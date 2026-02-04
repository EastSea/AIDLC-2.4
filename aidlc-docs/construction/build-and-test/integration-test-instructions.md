# Integration Test Instructions

## Prerequisites
- Infrastructure 실행 중 (PostgreSQL, Redis)
- Backend API 또는 Mock Server 실행 중

## 1. MCP + Mock Server 통합 테스트

### 1.1 Mock Server 시작
```bash
cd mock
python mock-server.py
```

### 1.2 Customer MCP 테스트
```bash
export API_URL=http://localhost:8001/api
export REDIS_URL=redis://localhost:6379

# MCP Server 시작 후 별도 터미널에서 테스트
cd mcp/customer
python -c "
import asyncio
from server import client, session_manager
import redis.asyncio as redis

async def test():
    r = redis.from_url('redis://localhost:6379')
    from mcp_core import SessionManager
    sm = SessionManager(r)
    
    # 1. 컨텍스트 설정
    from tools.context import set_table_context
    result = await set_table_context(client, sm, 'test-sess', 'STORE001', 1, '1234')
    print('set_table_context:', result)
    
    # 2. 카테고리 조회
    from tools.menu import get_categories
    result = await get_categories(client, sm, 'test-sess')
    print('get_categories:', result)

asyncio.run(test())
"
```

### 1.3 Admin MCP 테스트
```bash
cd mcp/admin
python -c "
import asyncio
from server import client
import redis.asyncio as redis

async def test():
    r = redis.from_url('redis://localhost:6379')
    from mcp_core import SessionManager
    sm = SessionManager(r)
    
    # 1. 관리자 컨텍스트 설정
    from tools.context import set_admin_context
    result = await set_admin_context(client, sm, 'admin-sess', 'STORE001', 'admin', 'admin123')
    print('set_admin_context:', result)
    
    # 2. 주문 조회
    from tools.order import get_orders
    result = await get_orders(client, sm, 'admin-sess')
    print('get_orders:', result)

asyncio.run(test())
"
```

## 2. End-to-End 시나리오

### 고객 주문 플로우
1. `set_table_context` → 테이블 로그인
2. `get_categories` → 카테고리 조회
3. `get_menus` → 메뉴 조회
4. `add_to_cart` → 장바구니 추가
5. `place_order` → 주문 생성
6. `get_orders` → 주문 확인

### 관리자 주문 관리 플로우
1. `set_admin_context` → 관리자 로그인
2. `get_orders` → 주문 목록 조회
3. `update_order_status` → 상태 변경 (pending → preparing → completed)
4. `complete_table` → 테이블 완료 처리
