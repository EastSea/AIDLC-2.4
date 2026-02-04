# Unit 3 (MCP Servers) - Functional Design

## 1. 아키텍처 개요

```
┌─────────────────────────────────────────────────────────────┐
│                      MCP Servers                            │
├─────────────────┬─────────────────┬─────────────────────────┤
│  customer-mcp   │   admin-mcp     │       mcp-core          │
│  (고객용 MCP)   │  (관리자 MCP)   │     (공유 모듈)         │
├─────────────────┴─────────────────┴─────────────────────────┤
│                        Redis                                │
│              (세션 관리: mcp:{session_id})                  │
├─────────────────────────────────────────────────────────────┤
│                     Backend API                             │
│                   (localhost:8000)                          │
└─────────────────────────────────────────────────────────────┘
```

## 2. mcp-core (공유 모듈)

### 2.1 TableOrderClient
Backend API 호출을 위한 HTTP 클라이언트

```python
class TableOrderClient:
    base_url: str
    
    # Customer API
    async def login(store_code, table_number) -> LoginResponse
    async def get_categories(token) -> List[Category]
    async def get_menus(token, category_id?) -> List[Menu]
    async def create_order(token, items) -> Order
    async def get_orders(token) -> List[Order]
    async def call_staff(token, call_type) -> StaffCall
    
    # Admin API
    async def admin_login(username, password) -> AdminLoginResponse
    async def get_all_orders(token, status?) -> List[Order]
    async def update_order_status(token, order_id, status) -> Order
    async def complete_table(token, table_id) -> Table
    async def get_menus_admin(token) -> List[Menu]
    async def update_menu(token, menu_id, data) -> Menu
```

### 2.2 SessionManager
Redis 기반 세션 관리

```python
class SessionManager:
    redis: Redis
    
    async def save_context(session_id, context: dict) -> None
    async def get_context(session_id) -> dict | None
    async def delete_context(session_id) -> None
    async def is_valid(session_id) -> bool
```

### 2.3 Response Models

```python
class ToolResponse:
    success: bool
    data: Any | None
    error: str | None

class CustomerContext:
    session_id: str
    store_code: str
    table_number: int
    token: str
    table_id: int

class AdminContext:
    session_id: str
    username: str
    token: str
    store_id: int
```

## 3. Customer MCP Tools

| Tool | 설명 | 전제조건 |
|------|------|----------|
| `set_table_context` | 테이블 컨텍스트 설정 | 없음 |
| `get_categories` | 카테고리 목록 조회 | 컨텍스트 필요 |
| `get_menus` | 메뉴 목록 조회 | 컨텍스트 필요 |
| `add_to_cart` | 장바구니 추가 | 컨텍스트 필요 |
| `view_cart` | 장바구니 조회 | 컨텍스트 필요 |
| `place_order` | 주문 생성 | 컨텍스트 필요 |
| `get_orders` | 주문 내역 조회 | 컨텍스트 필요 |
| `call_staff` | 직원 호출 | 컨텍스트 필요 |

### 3.1 Tool 상세

#### set_table_context
```
Input:  store_code (str), table_number (int)
Output: ToolResponse { success, data: { table_id, store_name } }
Flow:   1. Backend login API 호출
        2. Redis에 컨텍스트 저장 (key: mcp:{session_id})
        3. 결과 반환
```

#### add_to_cart
```
Input:  menu_id (int), quantity (int), options? (str)
Output: ToolResponse { success, data: { cart_items, total } }
Flow:   1. 컨텍스트 검증
        2. Backend cart API 호출
        3. 결과 반환
```

#### place_order
```
Input:  없음 (장바구니 기반)
Output: ToolResponse { success, data: { order_id, items, total } }
Flow:   1. 컨텍스트 검증
        2. Backend order API 호출
        3. 결과 반환
```

## 4. Admin MCP Tools

| Tool | 설명 | 전제조건 |
|------|------|----------|
| `set_admin_context` | 관리자 컨텍스트 설정 | 없음 |
| `get_orders` | 주문 목록 조회 | 컨텍스트 필요 |
| `update_order_status` | 주문 상태 변경 | 컨텍스트 필요 |
| `complete_table` | 테이블 완료 처리 | 컨텍스트 필요 |
| `get_menus` | 메뉴 목록 조회 | 컨텍스트 필요 |
| `update_menu` | 메뉴 수정 | 컨텍스트 필요 |

### 4.1 Tool 상세

#### set_admin_context
```
Input:  username (str), password (str)
Output: ToolResponse { success, data: { store_name, admin_name } }
Flow:   1. Backend admin login API 호출
        2. Redis에 컨텍스트 저장
        3. 결과 반환
```

#### update_order_status
```
Input:  order_id (int), status (str: pending|preparing|ready|completed)
Output: ToolResponse { success, data: { order_id, new_status } }
Flow:   1. 컨텍스트 검증
        2. Backend API 호출
        3. 결과 반환
```

## 5. 비즈니스 규칙

### 5.1 컨텍스트 검증
- 모든 Tool (set_*_context 제외)은 유효한 컨텍스트 필요
- 컨텍스트 없으면: `{ success: false, error: "컨텍스트가 설정되지 않았습니다. set_table_context를 먼저 호출해주세요." }`

### 5.2 세션 만료
- Redis TTL: 3600초 (1시간)
- 만료 시: `{ success: false, error: "세션이 만료되었습니다. 다시 로그인해주세요." }`

### 5.3 에러 응답 형식
```python
# 성공
{ "success": True, "data": {...}, "error": None }

# 실패
{ "success": False, "data": None, "error": "에러 메시지" }
```

## 6. 데이터 흐름

### 6.1 고객 주문 흐름
```
1. set_table_context(store_code, table_number)
   └─> Redis 저장, token 획득

2. get_categories() → get_menus(category_id)
   └─> 메뉴 탐색

3. add_to_cart(menu_id, quantity) [반복]
   └─> Backend cart API

4. place_order()
   └─> Backend order API

5. get_orders()
   └─> 주문 확인
```

### 6.2 관리자 주문 관리 흐름
```
1. set_admin_context(username, password)
   └─> Redis 저장, admin token 획득

2. get_orders(status="pending")
   └─> 대기 주문 조회

3. update_order_status(order_id, "preparing")
   └─> 상태 변경

4. complete_table(table_id)
   └─> 테이블 완료 처리
```
