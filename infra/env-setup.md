# Environment Setup Guide

## Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js 18+

## 1. 로컬 개발 환경 시작

### 1.1 Docker 서비스 시작
```bash
cd infra
docker-compose up -d
```

### 1.2 서비스 확인
```bash
# PostgreSQL 확인
docker exec -it table-order-postgres psql -U tableorder -c "SELECT 1"

# Redis 확인
docker exec -it table-order-redis redis-cli ping
```

### 1.3 서비스 중지
```bash
docker-compose down
```

## 2. 접속 정보

| Service | Host | Port | Credentials |
|---------|------|------|-------------|
| PostgreSQL | localhost | 5432 | tableorder / tableorder123 |
| Redis | localhost | 6379 | - |

### Database URL
```
postgresql://tableorder:tableorder123@localhost:5432/tableorder
```

### Redis URL
```
redis://localhost:6379
```

## 3. Backend API 실행

```bash
cd api
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# DB 마이그레이션
alembic upgrade head

# 서버 실행
uvicorn app.main:app --reload --port 8000
```

API 문서: http://localhost:8000/docs

## 4. Mock API 실행

```bash
cd mock
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 mock-server.py
```

Mock API: http://localhost:8001

## 5. Frontend 실행

```bash
cd web
npm install
npm start
```

Frontend: http://localhost:3000

## 6. MCP Server 실행

### 6.1 mcp-core 설치 (공통)
```bash
cd mcp/core
pip install -e .
```

### 6.2 Customer MCP
```bash
cd mcp/customer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e ../core

# 환경 변수 설정
export API_URL=http://localhost:8001/api  # Mock Server
export REDIS_URL=redis://localhost:6379

python server.py
```

### 6.3 Admin MCP
```bash
cd mcp/admin
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e ../core

# 환경 변수 설정
export API_URL=http://localhost:8001/api  # Mock Server
export REDIS_URL=redis://localhost:6379

python server.py
```

## 7. MCP Inspector 테스트

MCP Server를 Inspector로 테스트하려면:

### 7.1 Customer MCP Inspector
```bash
cd mcp/customer
source venv/bin/activate
export API_URL=http://localhost:8001/api
export REDIS_URL=redis://localhost:6379

npx @modelcontextprotocol/inspector python server.py
```

브라우저에서 `http://localhost:5173` 접속

### 7.2 테스트 시나리오

**Customer MCP:**
1. `set_table_context` → `{"store_code": "STORE001", "table_number": 1, "password": "1234"}`
2. `get_categories` → (파라미터 없음)
3. `get_menus` → `{"category_id": "cat-1"}`
4. `add_to_cart` → `{"menu_id": "menu-1", "quantity": 2}`
5. `place_order` → (파라미터 없음)

**Admin MCP:**
1. `set_admin_context` → `{"store_code": "STORE001", "username": "admin", "password": "admin123"}`
2. `get_orders` → (파라미터 없음)
3. `update_order_status` → `{"order_id": "order-1", "status": "preparing"}`

## 8. 환경 변수 요약

| 변수 | 값 | 용도 |
|------|-----|------|
| `DATABASE_URL` | `postgresql://tableorder:tableorder123@localhost:5432/tableorder` | Backend |
| `REDIS_URL` | `redis://localhost:6379` | Backend, MCP |
| `API_URL` | `http://localhost:8000/api` (실서버) / `http://localhost:8001/api` (Mock) | MCP |
