# Build Instructions

## Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js 18+

## 1. Infrastructure 시작

```bash
cd infra
docker-compose up -d
```

확인:
- PostgreSQL: `localhost:5432`
- Redis: `localhost:6379`

## 2. Backend (Unit 1 - 미완료)

```bash
cd api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

## 3. Mock Server (개발용)

```bash
cd mock
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
python mock-server.py
```

Mock API: `http://localhost:8001`

## 4. Frontend (Unit 2 - 미완료)

```bash
cd web
npm install
npm start
```

## 5. MCP Servers (Unit 3)

### mcp-core 설치
```bash
cd mcp/core
pip install -e .
```

### customer-mcp
```bash
cd mcp/customer
pip install -r requirements.txt
python server.py
```

### admin-mcp
```bash
cd mcp/admin
pip install -r requirements.txt
python server.py
```

## 환경 변수

```bash
# MCP Servers
export API_URL=http://localhost:8000/api
export REDIS_URL=redis://localhost:6379

# Backend
export DATABASE_URL=postgresql://tableorder:tableorder123@localhost:5432/tableorder
export REDIS_URL=redis://localhost:6379
```
