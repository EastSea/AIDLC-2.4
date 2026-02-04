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

```bash
# Customer MCP
cd mcp/customer
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 -m customer_mcp

# Admin MCP
cd mcp/admin
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 -m admin_mcp
```
