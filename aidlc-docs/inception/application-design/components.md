# Components Definition

## System Architecture Overview

```
+-------------------+      +-------------------+      +-------------------+
|    Frontend       |      |    Backend API    |      |    Database       |
|    (React SPA)    |<---->|    (FastAPI)      |<---->|    (PostgreSQL)   |
+-------------------+      +-------------------+      +-------------------+
         ^                          ^
         |                          |
         v                          v
+-------------------+      +-------------------+
|  Customer MCP     |      |  Admin MCP        |
|  Server           |      |  Server           |
+-------------------+      +-------------------+
```

---

## 1. Frontend (React SPA)

### 1.1 프로젝트 구조
- **프로젝트**: 단일 React 프로젝트
- **라우팅**: React Router로 고객/관리자 분리
  - `/customer/*` - 고객용 화면
  - `/admin/*` - 관리자용 화면

### 1.2 고객용 컴포넌트

| Component | Responsibility |
|-----------|----------------|
| `TableLogin` | 테이블 초기 설정 및 자동 로그인 |
| `MenuList` | 카테고리별 메뉴 목록 표시 |
| `MenuCard` | 개별 메뉴 카드 (이미지, 이름, 가격) |
| `MenuDetail` | 메뉴 상세 정보 모달 |
| `CategoryNav` | 좌측 카테고리 네비게이션 |
| `PersonFilter` | 인원수 필터 (전체, 1~2인, 3~4인) |
| `Cart` | 장바구니 관리 |
| `CartItem` | 장바구니 개별 항목 |
| `OrderConfirm` | 주문 확인 및 확정 |
| `OrderSuccess` | 주문 성공 화면 (주문번호 표시) |
| `OrderHistory` | 주문 내역 조회 |
| `OrderStatusBadge` | 주문 상태 표시 (대기중/준비중/완료) |
| `IdleTimer` | 60초 Idle Timeout 관리 및 카운트다운 표시 |
| `StaffCall` | 직원 호출 버튼 |
| `TableInfo` | 우측 상단 테이블 번호 표시 |

### 1.3 관리자용 컴포넌트

| Component | Responsibility |
|-----------|----------------|
| `AdminLogin` | 관리자 로그인 (매장ID, 사용자명, 비밀번호) |
| `Dashboard` | 실시간 주문 대시보드 (그리드 레이아웃) |
| `TableCard` | 테이블별 주문 카드 (총 주문액, 최신 주문 미리보기) |
| `OrderDetail` | 주문 상세 모달 (전체 메뉴 목록) |
| `OrderStatusControl` | 주문 상태 변경 버튼 |
| `TableManagement` | 테이블 관리 (이용 완료, 주문 삭제) |
| `OrderHistoryAdmin` | 과거 주문 내역 조회 (날짜 필터) |
| `MenuManagement` | 메뉴 CRUD 관리 화면 |
| `MenuForm` | 메뉴 등록/수정 폼 |
| `MenuImageUpload` | 메뉴 이미지 업로드 |
| `StaffCallAlert` | 직원 호출 알림 표시 |
| `NewOrderAlert` | 신규 주문 시각적 강조 |

---

## 2. Backend API (FastAPI)

### 2.1 프로젝트 구조
- **프로젝트**: 단일 FastAPI 앱
- **라우터 분리**:
  - `/api/customer/*` - 고객용 API
  - `/api/admin/*` - 관리자용 API
  - `/api/sse/*` - SSE 실시간 스트림

### 2.2 레이어 구조

```
+---------------------+
|      Routers        |  API 엔드포인트 정의
+---------------------+
          |
+---------------------+
|      Schemas        |  Pydantic 요청/응답 모델
+---------------------+
          |
+---------------------+
|      Services       |  비즈니스 로직
+---------------------+
          |
+---------------------+
|    Repositories     |  데이터 접근 계층
+---------------------+
          |
+---------------------+
|       Models        |  SQLAlchemy ORM 모델
+---------------------+
```

### 2.3 서비스 컴포넌트

| Service | Responsibility |
|---------|----------------|
| `AuthService` | JWT 발급/검증, 테이블 로그인, 관리자 로그인, 세션 관리 |
| `MenuService` | 메뉴 CRUD, 카테고리 관리, 인원수 태그 관리, 순서 조정 |
| `CartService` | 장바구니 관리 (테이블 세션 기반) |
| `OrderService` | 주문 생성, 상태 변경, 조회, 삭제, 과거 이력 관리 |
| `TableService` | 테이블 세션 시작/종료, 이용 완료 처리 |
| `SSEService` | 실시간 이벤트 브로드캐스트 (주문, 상태변경, 직원호출) |
| `StaffCallService` | 직원 호출 생성, 조회, 응답 처리 |
| `ImageService` | 이미지 업로드, 저장 (PostgreSQL BYTEA), 조회 |

### 2.4 SSE 엔드포인트

| Endpoint | Purpose |
|----------|---------|
| `GET /api/sse/orders` | 관리자용 - 새 주문 및 상태 변경 이벤트 |
| `GET /api/sse/order-status/{table_id}` | 고객용 - 해당 테이블 주문 상태 변경 |
| `GET /api/sse/staff-calls` | 관리자용 - 직원 호출 알림 |

---

## 3. MCP Servers

### 3.1 Architecture (공유 서비스 모듈)

```
+------------------+     +------------------+
| Customer MCP     |     | Admin MCP        |
| Server           |     | Server           |
+------------------+     +------------------+
         |                       |
         +-----------+-----------+
                     |
                     v
         +---------------------+
         |  Shared Service     |
         |  Module (mcp-core)  |
         +---------------------+
                     |
                     v
         +---------------------+
         |  Backend API        |
         |  (FastAPI)          |
         +---------------------+
```

- **mcp-core**: 공유 서비스 모듈 (API 클라이언트, 공통 로직)
- **customer-mcp**: 고객용 MCP Server (mcp-core 확장)
- **admin-mcp**: 관리자용 MCP Server (mcp-core 확장)

### 3.2 Customer MCP Server
- **역할**: 고객용 Chatbot 연동
- **프로젝트**: 별도 Python 프로젝트 (mcp-core 의존)
- **필수 사전 체크**: 모든 Tool 호출 전 테이블 식별 필수

| Tool | Description | Pre-check |
|------|-------------|-----------|
| `set_table_context` | **테이블 컨텍스트 설정 (필수 최초 호출)** | - |
| `get_table_info` | 현재 테이블 정보 조회 | table_context |
| `get_menu_list` | 메뉴 목록 조회 (카테고리, 인원수 필터) | table_context |
| `get_menu_detail` | 메뉴 상세 정보 조회 | table_context |
| `add_to_cart` | 장바구니에 메뉴 추가 | table_context |
| `update_cart_item` | 장바구니 항목 수량 변경 | table_context |
| `remove_from_cart` | 장바구니에서 항목 삭제 | table_context |
| `get_cart` | 현재 장바구니 조회 | table_context |
| `clear_cart` | 장바구니 비우기 | table_context |
| `create_order` | 주문 생성 | table_context |
| `get_order_history` | 현재 세션 주문 내역 조회 | table_context |
| `get_order_status` | 특정 주문 상태 조회 | table_context |
| `call_staff` | 직원 호출 | table_context |

### 3.3 Admin MCP Server
- **역할**: 관리자용 Chatbot 연동
- **프로젝트**: 별도 Python 프로젝트 (mcp-core 의존)

| Tool | Description |
|------|-------------|
| `set_admin_context` | **관리자 컨텍스트 설정 (필수 최초 호출)** |
| `get_orders` | 현재 주문 현황 조회 (테이블별) |
| `get_order_detail` | 특정 주문 상세 조회 |
| `update_order_status` | 주문 상태 변경 (대기중→준비중→완료) |
| `delete_order` | 주문 삭제 |
| `complete_table_session` | 테이블 이용 완료 처리 |
| `get_order_history` | 과거 주문 내역 조회 (날짜 필터) |
| `get_menus` | 메뉴 목록 조회 |
| `get_menu_detail` | 메뉴 상세 조회 |
| `create_menu` | 메뉴 등록 |
| `update_menu` | 메뉴 수정 |
| `delete_menu` | 메뉴 삭제 |
| `get_staff_calls` | 직원 호출 목록 조회 |

---

## 4. Database (PostgreSQL)

### 4.1 스키마 관리
- **도구**: Alembic (SQLAlchemy 마이그레이션)
- **전략**: 버전 관리 기반 마이그레이션

### 4.2 테이블 목록

| Table | Description |
|-------|-------------|
| `stores` | 매장 정보 |
| `admin_users` | 관리자 계정 |
| `tables` | 테이블 정보 |
| `table_sessions` | 테이블 세션 (고객 이용 단위) |
| `categories` | 메뉴 카테고리 |
| `menus` | 메뉴 정보 |
| `menu_images` | 메뉴 이미지 (BYTEA 저장) |
| `orders` | 주문 정보 |
| `order_items` | 주문 항목 |
| `order_history` | 완료된 주문 이력 |
| `staff_calls` | 직원 호출 기록 |
