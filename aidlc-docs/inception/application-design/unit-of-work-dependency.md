# Unit of Work Dependencies

## Dependency Matrix

| Unit | Depends On | Depended By |
|------|------------|-------------|
| **Unit 0 (Common)** | - | Unit 1, 2, 3 |
| **Unit 1 (Backend)** | Unit 0 | Unit 2, 3 (실제 API 전환 시) |
| **Unit 2 (Frontend)** | Unit 0 (Mock API) | - |
| **Unit 3 (MCP)** | Unit 0 (Mock API) | - |

---

## Dependency Diagram

```
                    +------------------+
                    |   Unit 0         |
                    |   (Common)       |
                    | - Infrastructure |
                    | - OpenAPI Spec   |
                    | - Mock API       |
                    | - env-setup.md   |
                    +------------------+
                            |
          +-----------------+-----------------+
          |                 |                 |
          v                 v                 v
+------------------+ +------------------+ +------------------+
|   Unit 1         | |   Unit 2         | |   Unit 3         |
|   (Backend)      | |   (Frontend)     | |   (MCP)          |
| - FastAPI        | | - React          | | - mcp-core       |
| - PostgreSQL     | | - Mock → Real    | | - customer-mcp   |
| - Redis          | |                  | | - admin-mcp      |
| - SSE            | |                  | |                  |
+------------------+ +------------------+ +------------------+
          |                 ^                 ^
          |                 |                 |
          +-----------------+-----------------+
                    (Phase 3: 실제 API 전환)
```

---

## Parallel Development Strategy

### 병렬 개발 가능 영역

| Phase | Backend | Frontend | MCP | 블로킹 |
|-------|---------|----------|-----|--------|
| 0 | ✅ 협업 | ✅ 협업 | ✅ 협업 | 없음 |
| 1 | ✅ 독립 | ✅ Mock 사용 | ✅ Mock 사용 | 없음 |
| 2 | ✅ 독립 | ✅ Mock 사용 | ✅ Mock 사용 | 없음 |
| 3 | ✅ 완성 | ⚠️ API 대기 | ⚠️ API 대기 | Backend 완료 필요 |
| 4 | ✅ 통합 | ✅ 통합 | ✅ 통합 | 없음 |

### 통합 포인트

| 시점 | 통합 내용 |
|------|----------|
| Phase 0 완료 | OpenAPI 스펙 확정, Mock API 검증 |
| Phase 1 완료 | 고객용 기능 통합 테스트 |
| Phase 2 완료 | 관리자용 기능 통합 테스트 |
| Phase 3 완료 | Mock → 실제 API 전환 완료 |
| Phase 4 완료 | 전체 E2E 테스트 |

---

## Critical Path

```
Phase 0 (공통) → Phase 1~2 (병렬) → Phase 3 (API 전환) → Phase 4 (통합)
     |                                      |
     |                                      |
     +--- Mock API로 블로킹 최소화 ---+
```

**핵심**: Phase 0에서 Mock API를 완성하면 Backend 완료 전까지 Frontend/MCP가 블로킹 없이 개발 가능
