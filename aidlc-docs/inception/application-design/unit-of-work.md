# Unit of Work Definition

## Team Structure
- **팀 규모**: 3명
- **분배 방식**: 레이어별 분배
- **통합 시점**: Phase 완료 시
- **API 계약**: OpenAPI (Swagger) 스펙 + Mock API

---

## Directory Structure

```
/api                    # Backend API (개발자 1)
  /app
    /routers
    /services
    /repositories
    /models
    /schemas
  /alembic
  /tests
  requirements.txt
  main.py

/web                    # Frontend (개발자 2)
  /src
    /components
    /pages
    /hooks
    /services
    /styles
  package.json

/mcp                    # MCP Servers (개발자 3)
  /core
  /customer
  /admin

/infra                  # Infrastructure (공통)
  docker-compose.yml
  Dockerfile.api
  Dockerfile.web
  env-setup.md          # 환경 설정 가이드

/docs                   # API 스펙 (공통)
  openapi.yaml

/mock                   # Mock API (공통)
  mock-server.py
  requirements.txt
```

---

## Unit Definitions

### Unit 0: Common (공통 선행 - 3명 협업)

| 항목 | 내용 |
|------|------|
| **담당자** | 3명 공동 |
| **디렉토리** | `/infra`, `/docs`, `/mock` |
| **주요 책임** | Infrastructure, OpenAPI 스펙, Mock API, 환경 설정 문서 |

**산출물**:
- Docker Compose (PostgreSQL + Redis)
- OpenAPI 스펙 (`/docs/openapi.yaml`)
- Mock API Server (`/mock`)
- 환경 설정 가이드 (`/infra/env-setup.md`)

---

### Unit 1: Backend API (개발자 1)

| 항목 | 내용 |
|------|------|
| **담당자** | 개발자 1 |
| **디렉토리** | `/api` |
| **기술 스택** | Python, FastAPI, SQLAlchemy, Alembic, Redis |
| **주요 책임** | REST API, SSE, DB 모델, 인증, 세션(Redis) |

---

### Unit 2: Frontend (개발자 2)

| 항목 | 내용 |
|------|------|
| **담당자** | 개발자 2 |
| **디렉토리** | `/web` |
| **기술 스택** | React, React Router, Axios |
| **주요 책임** | 고객용 UI, 관리자용 UI, 반응형 |

---

### Unit 3: MCP Servers (개발자 3)

| 항목 | 내용 |
|------|------|
| **담당자** | 개발자 3 |
| **디렉토리** | `/mcp` |
| **기술 스택** | Python, MCP SDK, httpx |
| **주요 책임** | mcp-core, customer-mcp, admin-mcp |

---

## Development Phases

```
+------------------------------------------------------------------+
|                    Phase 0: 공통 선행 (3명 협업)                    |
|  Infrastructure + OpenAPI + Mock API + env-setup.md               |
+------------------------------------------------------------------+
                              |
                              v
+------------------+  +------------------+  +------------------+
|    Phase 1~3     |  |    Phase 1~3     |  |    Phase 1~3     |
|   Backend API    |  |    Frontend      |  |   MCP Servers    |
|    (개발자 1)     |  |    (개발자 2)     |  |    (개발자 3)     |
+------------------+  +------------------+  +------------------+
                              |
                              v
+------------------------------------------------------------------+
|                    Phase 4: 통합 및 테스트                         |
+------------------------------------------------------------------+
```

### Phase 0: 공통 선행 (3명 협업) ⭐

| 작업 | 산출물 |
|------|--------|
| Docker Compose (PostgreSQL + Redis) | `/infra/docker-compose.yml` |
| 환경 설정 가이드 | `/infra/env-setup.md` |
| DB 스키마 설계 | `/api/alembic` |
| OpenAPI 스펙 정의 | `/docs/openapi.yaml` |
| Mock API Server | `/mock/mock-server.py` |

**완료 조건**: 
- `docker-compose up`으로 PostgreSQL + Redis 실행 가능
- Mock API Server로 Frontend/MCP 개발 시작 가능

### Phase 1~3: 개별 개발 (병렬)

| Phase | 개발자 1 (Backend) | 개발자 2 (Frontend) | 개발자 3 (MCP) |
|-------|-------------------|---------------------|----------------|
| 1 | 고객용 API 구현 | 고객용 UI (Mock 연동) | 고객용 MCP (Mock 연동) |
| 2 | 관리자용 API + SSE | 관리자용 UI | 관리자용 MCP |
| 3 | API 완성 | Mock → 실제 API 전환 | Mock → 실제 API 전환 |

### Phase 4: 통합 테스트
- E2E 테스트
- 성능 테스트
- 버그 수정
