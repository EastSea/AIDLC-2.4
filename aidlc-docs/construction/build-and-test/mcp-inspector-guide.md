# MCP Inspector 로컬 테스트 환경

## Prerequisites
- Node.js 18+
- Docker (Redis용)
- Mock Server 실행

## 1. Infrastructure 시작

```bash
cd infra
docker-compose up -d redis
```

## 2. Mock Server 시작

```bash
cd mock
python3 mock-server.py
```

## 3. MCP Inspector 설치 및 실행

### Customer MCP 테스트
```bash
cd mcp/customer
source venv/bin/activate

# 환경 변수 설정
export API_URL=http://localhost:8001/api
export REDIS_URL=redis://localhost:6379

# MCP Inspector 실행
npx @modelcontextprotocol/inspector python server.py
```

### Admin MCP 테스트
```bash
cd mcp/admin
source venv/bin/activate

# 환경 변수 설정
export API_URL=http://localhost:8001/api
export REDIS_URL=redis://localhost:6379

# MCP Inspector 실행
npx @modelcontextprotocol/inspector python server.py
```

## 4. Inspector 사용법

브라우저에서 `http://localhost:5173` 접속

### Customer MCP 테스트 시나리오

1. **set_table_context** 호출
   ```json
   {
     "store_code": "STORE001",
     "table_number": 1,
     "password": "1234"
   }
   ```

2. **get_categories** 호출 (파라미터 없음)

3. **get_menus** 호출
   ```json
   {
     "category_id": "cat-1"
   }
   ```

4. **add_to_cart** 호출
   ```json
   {
     "menu_id": "menu-1",
     "quantity": 2
   }
   ```

5. **view_cart** 호출 (파라미터 없음)

6. **place_order** 호출 (파라미터 없음)

7. **get_orders** 호출 (파라미터 없음)

8. **call_staff** 호출 (파라미터 없음)

### Admin MCP 테스트 시나리오

1. **set_admin_context** 호출
   ```json
   {
     "store_code": "STORE001",
     "username": "admin",
     "password": "admin123"
   }
   ```

2. **get_orders** 호출 (파라미터 없음)

3. **update_order_status** 호출
   ```json
   {
     "order_id": "order-1",
     "status": "preparing"
   }
   ```

4. **get_menus** 호출 (파라미터 없음)

5. **complete_table** 호출
   ```json
   {
     "table_id": "table-1"
   }
   ```

## 5. 트러블슈팅

### Redis 연결 실패
```bash
# Redis 상태 확인
docker ps | grep redis

# Redis 재시작
docker-compose restart redis
```

### Mock Server 연결 실패
```bash
# Mock Server 포트 확인
lsof -i :8001
```

### MCP Inspector 설치 오류
```bash
# npm 캐시 정리 후 재시도
npm cache clean --force
npx @modelcontextprotocol/inspector python server.py
```
