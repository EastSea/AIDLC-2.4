# Unit 1 (Backend API) - Code Generation Plan

## Overview
Backend API 구현: FastAPI + SQLAlchemy + Alembic + Redis

---

## Unit Context
- **Unit Name**: Backend API (Unit 1)
- **담당**: 개발자 1
- **디렉토리**: `/api`
- **기술 스택**: Python, FastAPI, SQLAlchemy, Alembic, Redis
- **주요 책임**: REST API, SSE, DB 모델, 인증, 세션(Redis)

---

## Dependencies
- **Depends On**: Unit 0 (Common) - Infrastructure, OpenAPI Spec
- **Depended By**: Unit 2 (Frontend), Unit 3 (MCP) - Phase 3 실제 API 전환 시

---

## Story Mapping

### 고객용 API (Phase 1)
| Story ID | Story Name | Priority |
|----------|------------|----------|
| US-1.1 | 테이블 초기 설정 | High |
| US-1.2 | 자동 로그인 | High |
| US-2.1 | 카테고리별 메뉴 조회 | High |
| US-2.2 | 메뉴 상세 정보 확인 | Medium |
| US-2.3 | 인원수별 메뉴 필터 | Medium |
| US-4.1 | 주문 확정 | High |
| US-4.2 | 주문 실패 처리 | High |
| US-5.1 | 현재 세션 주문 조회 | High |
| US-5.2 | 주문 상태 확인 | Medium |
| US-6.3 | 직원 호출 | Low |

### 관리자용 API (Phase 2)
| Story ID | Story Name | Priority |
|----------|------------|----------|
| US-7.1 | 관리자 로그인 | High |
| US-7.2 | 자동 로그아웃 | Medium |
| US-8.1 | 실시간 주문 대시보드 (SSE) | High |
| US-8.2 | 주문 상태 변경 | High |
| US-8.3 | 주문 상세 보기 | Medium |
| US-9.1 | 주문 삭제 | Medium |
| US-9.2 | 테이블 이용 완료 | High |
| US-9.3 | 과거 주문 내역 조회 | Low |
| US-10.1 | 메뉴 조회 | High |
| US-10.2 | 메뉴 등록 | High |
| US-10.3 | 메뉴 수정 | Medium |
| US-10.4 | 메뉴 삭제 | Medium |
| US-10.5 | 메뉴 순서 조정 | Low |

---

## Generation Steps

### Phase 0: Database Models & Migration

#### Step 1: Database Models
**파일**: `/api/app/models/__init__.py`, `/api/app/models/*.py`

**생성할 모델**:
- `Store` - 매장 정보
- `AdminUser` - 관리자 계정
- `Table` - 테이블 정보
- `TableSession` - 테이블 세션
- `Category` - 메뉴 카테고리
- `Menu` - 메뉴
- `MenuImage` - 메뉴 이미지 (BYTEA)
- `Order` - 주문
- `OrderItem` - 주문 항목
- `StaffCall` - 직원 호출

**체크리스트**:
- [ ] `/api/app/models/__init__.py` 생성
- [ ] `/api/app/models/store.py` 생성
- [ ] `/api/app/models/admin_user.py` 생성
- [ ] `/api/app/models/table.py` 생성
- [ ] `/api/app/models/table_session.py` 생성
- [ ] `/api/app/models/category.py` 생성
- [ ] `/api/app/models/menu.py` 생성
- [ ] `/api/app/models/menu_image.py` 생성
- [ ] `/api/app/models/order.py` 생성
- [ ] `/api/app/models/order_item.py` 생성
- [ ] `/api/app/models/staff_call.py` 생성

#### Step 2: Alembic Setup
**파일**: `/api/alembic.ini`, `/api/alembic/env.py`

**체크리스트**:
- [ ] `alembic init alembic` 실행
- [ ] `/api/alembic.ini` 설정 (DB URL)
- [ ] `/api/alembic/env.py` 수정 (모델 import)
- [ ] 초기 마이그레이션 생성: `alembic revision --autogenerate -m "Initial migration"`
- [ ] 마이그레이션 적용: `alembic upgrade head`

#### Step 3: Pydantic Schemas
**파일**: `/api/app/schemas/__init__.py`, `/api/app/schemas/*.py`

**생성할 스키마**:
- `StoreSchema` - 매장 정보
- `AdminUserSchema` - 관리자 로그인/응답
- `TableSchema` - 테이블 정보
- `TableSessionSchema` - 세션 생성/응답
- `CategorySchema` - 카테고리 조회/생성/수정
- `MenuSchema` - 메뉴 조회/생성/수정
- `MenuImageSchema` - 메뉴 이미지
- `OrderSchema` - 주문 생성/조회/응답
- `OrderItemSchema` - 주문 항목
- `StaffCallSchema` - 직원 호출

**체크리스트**:
- [ ] `/api/app/schemas/__init__.py` 생성
- [ ] `/api/app/schemas/store.py` 생성
- [ ] `/api/app/schemas/admin_user.py` 생성
- [ ] `/api/app/schemas/table.py` 생성
- [ ] `/api/app/schemas/table_session.py` 생성
- [ ] `/api/app/schemas/category.py` 생성
- [ ] `/api/app/schemas/menu.py` 생성
- [ ] `/api/app/schemas/menu_image.py` 생성
- [ ] `/api/app/schemas/order.py` 생성
- [ ] `/api/app/schemas/staff_call.py` 생성

---

### Phase 1: 고객용 API

#### Step 4: Repositories (Data Access Layer)
**파일**: `/api/app/repositories/__init__.py`, `/api/app/repositories/*.py`

**생성할 Repository**:
- `TableRepository` - 테이블 CRUD
- `TableSessionRepository` - 세션 CRUD
- `CategoryRepository` - 카테고리 조회
- `MenuRepository` - 메뉴 조회
- `MenuImageRepository` - 메뉴 이미지 CRUD
- `OrderRepository` - 주문 CRUD
- `OrderItemRepository` - 주문 항목 CRUD
- `StaffCallRepository` - 직원 호출 CRUD

**체크리스트**:
- [ ] `/api/app/repositories/__init__.py` 생성
- [ ] `/api/app/repositories/table.py` 생성
- [ ] `/api/app/repositories/table_session.py` 생성
- [ ] `/api/app/repositories/category.py` 생성
- [ ] `/api/app/repositories/menu.py` 생성
- [ ] `/api/app/repositories/menu_image.py` 생성
- [ ] `/api/app/repositories/order.py` 생성
- [ ] `/api/app/repositories/order_item.py` 생성
- [ ] `/api/app/repositories/staff_call.py` 생성

#### Step 5: Services (Business Logic)
**파일**: `/api/app/services/__init__.py`, `/api/app/services/*.py`

**생성할 Service**:
- `AuthService` - 테이블/관리자 로그인, 세션 관리 (US-1.1, US-1.2, US-7.1)
- `MenuService` - 메뉴/카테고리 조회 (US-2.1, US-2.2, US-2.3)
- `OrderService` - 주문 처리 (US-4.1, US-4.2, US-5.1, US-5.2)
- `TableService` - 테이블 세션 관리
- `ImageService` - 메뉴 이미지 관리
- `StaffCallService` - 직원 호출 (US-6.3)

**체크리스트**:
- [ ] `/api/app/services/__init__.py` 생성
- [ ] `/api/app/services/auth.py` 생성
- [ ] `/api/app/services/menu.py` 생성
- [ ] `/api/app/services/order.py` 생성
- [ ] `/api/app/services/table.py` 생성
- [ ] `/api/app/services/image.py` 생성
- [ ] `/api/app/services/staff_call.py` 생성

#### Step 6: Redis Session Management
**파일**: `/api/app/redis.py`, `/api/app/dependencies.py`

**기능**:
- Redis 연결 설정
- 테이블 세션 저장/조회 (JWT 토큰 기반)
- 세션 의존성 주입

**체크리스트**:
- [ ] `/api/app/redis.py` 생성 (Redis 클라이언트)
- [ ] `/api/app/dependencies.py` 생성 (인증 의존성)
- [ ] JWT 토큰 검증 의존성 추가

#### Step 7: Customer Routers
**파일**: `/api/app/routers/__init__.py`, `/api/app/routers/customer/*.py`

**생성할 Router**:
- `auth.py` - 테이블 로그인 (POST /customer/auth/login)
- `category.py` - 카테고리 조회 (GET /customer/categories)
- `menu.py` - 메뉴 조회 (GET /customer/menus, GET /customer/menus/{id}, GET /customer/menus/{id}/image)
- `order.py` - 주문 관리 (POST /customer/orders, GET /customer/orders, GET /customer/orders/{id})
- `staff_call.py` - 직원 호출 (POST /customer/staff-call)

**체크리스트**:
- [ ] `/api/app/routers/__init__.py` 생성
- [ ] `/api/app/routers/customer/__init__.py` 생성
- [ ] `/api/app/routers/customer/auth.py` 생성
- [ ] `/api/app/routers/customer/category.py` 생성
- [ ] `/api/app/routers/customer/menu.py` 생성
- [ ] `/api/app/routers/customer/order.py` 생성
- [ ] `/api/app/routers/customer/staff_call.py` 생성

---

### Phase 2: 관리자용 API

#### Step 8: Admin Repositories
**파일**: `/api/app/repositories/admin/*.py`, `/api/app/repositories/*.py`

**추가 Repository**:
- `StoreRepository` - 매장 조회
- `AdminUserRepository` - 관리자 인증
- `AdminOrderRepository` - 관리자 주문 관리
- `AdminMenuRepository` - 메뉴 관리 (CRUD)
- `AdminCategoryRepository` - 카테고리 관리 (CRUD)
- `AdminTableRepository` - 테이블 관리
- `AdminStaffCallRepository` - 직원 호출 관리

**체크리스트**:
- [ ] `/api/app/repositories/admin/__init__.py` 생성
- [ ] `/api/app/repositories/store.py` 생성
- [ ] `/api/app/repositories/admin_user.py` 생성
- [ ] `/api/app/repositories/admin/order.py` 생성
- [ ] `/api/app/repositories/admin/menu.py` 생성
- [ ] `/api/app/repositories/admin/category.py` 생성
- [ ] `/api/app/repositories/admin/table.py` 생성
- [ ] `/api/app/repositories/admin/staff_call.py` 생성

#### Step 9: Admin Services
**파일**: `/api/app/services/admin/*.py`

**생성할 Service**:
- `AdminAuthService` - 관리자 로그인/로그아웃 (US-7.1, US-7.2)
- `AdminOrderService` - 주문 관리 (US-8.2, US-8.3, US-9.1, US-9.2, US-9.3)
- `AdminMenuService` - 메뉴 관리 (US-10.1~10.5)
- `AdminCategoryService` - 카테고리 관리
- `AdminTableService` - 테이블 관리
- `AdminStaffCallService` - 직원 호출 관리
- `SSEService` - 실시간 이벤트 브로드캐스트

**체크리스트**:
- [ ] `/api/app/services/admin/__init__.py` 생성
- [ ] `/api/app/services/admin/auth.py` 생성
- [ ] `/api/app/services/admin/order.py` 생성
- [ ] `/api/app/services/admin/menu.py` 생성
- [ ] `/api/app/services/admin/category.py` 생성
- [ ] `/api/app/services/admin/table.py` 생성
- [ ] `/api/app/services/admin/staff_call.py` 생성
- [ ] `/api/app/services/sse.py` 생성

#### Step 10: SSE (Server-Sent Events)
**파일**: `/api/app/sse.py`, `/api/app/routers/sse/*.py`

**기능**:
- 실시간 주문 대시보드 (US-8.1)
- Redis Pub/Sub 연동
- SSE 스트림 관리

**SSE 엔드포인트**:
- `GET /sse/orders` - 관리자용 주문 스트림 (new_order, order_status_changed, order_deleted)
- `GET /sse/order-status/{table_id}` - 고객용 상태 스트림 (order_status_changed)
- `GET /sse/staff-calls` - 관리자용 호출 스트림 (staff_call, staff_call_acknowledged)

**체크리스트**:
- [ ] `/api/app/sse.py` 생성 (SSE 핸들러)
- [ ] `/api/app/routers/sse/__init__.py` 생성
- [ ] `/api/app/routers/sse/orders.py` 생성
- [ ] `/api/app/routers/sse/staff_calls.py` 생성
- [ ] Redis Pub/Sub 설정
- [ ] 주문 상태 변경 시 이벤트 발행

#### Step 11: Admin Authentication
**파일**: `/api/app/auth.py`

**기능**:
- JWT 토큰 생성/검증
- 비밀번호 해싱 (bcrypt)
- 관리자 인증 의존성

**체크리스트**:
- [ ] `/api/app/auth.py` 생성
- [ ] JWT 토큰 생성 함수
- [ ] 비밀번호 해싱 함수
- [ ] 관리자 인증 의존성 (`get_current_admin`)

#### Step 12: Admin Routers
**파일**: `/api/app/routers/admin/*.py`

**생성할 Router**:
- `auth.py` - 로그인/로그아웃 (POST /admin/auth/login, POST /admin/auth/logout)
- `order.py` - 주문 관리 (GET /admin/orders, GET /admin/orders/{id}, PATCH /admin/orders/{id}/status, DELETE /admin/orders/{id}, GET /admin/orders/history)
- `table.py` - 테이블 관리 (GET /admin/tables, GET /admin/tables/{id}, POST /admin/tables/{id}/complete, GET /admin/tables/{id}/summary)
- `menu.py` - 메뉴 관리 (GET/POST/PUT/DELETE /admin/menus, POST /admin/menus/{id}/image, PATCH /admin/menus/order)
- `category.py` - 카테고리 관리 (GET/POST/PUT/DELETE /admin/categories)
- `staff_call.py` - 직원 호출 관리 (GET /admin/staff-calls, PATCH /admin/staff-calls/{id}/acknowledge)

**체크리스트**:
- [ ] `/api/app/routers/admin/__init__.py` 생성
- [ ] `/api/app/routers/admin/auth.py` 생성
- [ ] `/api/app/routers/admin/order.py` 생성
- [ ] `/api/app/routers/admin/table.py` 생성
- [ ] `/api/app/routers/admin/menu.py` 생성
- [ ] `/api/app/routers/admin/category.py` 생성
- [ ] `/api/app/routers/admin/staff_call.py` 생성

---

### Phase 3: API 완성 & 최적화

#### Step 13: Error Handling
**파일**: `/api/app/exceptions.py`, `/api/app/main.py`

**기능**:
- 커스텀 예외 정의
- 전역 예외 핸들러
- 에러 응답 표준화

**체크리스트**:
- [ ] `/api/app/exceptions.py` 생성
- [ ] 커스텀 예외 클래스 정의
- [ ] `main.py`에 예외 핸들러 등록

#### Step 14: Middleware
**파일**: `/api/app/middleware.py`

**기능**:
- CORS 설정
- 로깅 미들웨어
- 요청/응답 로깅

**체크리스트**:
- [ ] `/api/app/middleware.py` 생성
- [ ] CORS 미들웨어 설정
- [ ] 로깅 미들웨어 추가

#### Step 15: Testing
**파일**: `/api/tests/*.py`

**테스트 범위**:
- Unit Tests (Services, Repositories)
- Integration Tests (Routers)
- E2E Tests (전체 플로우)

**체크리스트**:
- [ ] `/api/tests/__init__.py` 생성
- [ ] `/api/tests/conftest.py` 생성 (pytest fixtures)
- [ ] `/api/tests/test_session.py` 생성
- [ ] `/api/tests/test_menu.py` 생성
- [ ] `/api/tests/test_order.py` 생성
- [ ] `/api/tests/test_admin.py` 생성

#### Step 16: Documentation
**파일**: `/api/README.md`

**내용**:
- API 실행 방법
- 환경 변수 설정
- 테스트 실행 방법
- API 엔드포인트 목록

**체크리스트**:
- [ ] `/api/README.md` 생성

---

## Completion Criteria

### Phase 1 완료 조건
- [ ] 고객용 API 10개 Story 구현 완료
- [ ] 세션 관리 (Redis) 동작 확인
- [ ] 메뉴 조회 API 동작 확인
- [ ] 주문 생성/조회 API 동작 확인
- [ ] OpenAPI 문서 자동 생성 확인 (`/docs`)

### Phase 2 완료 조건
- [ ] 관리자용 API 13개 Story 구현 완료
- [ ] 관리자 로그인/인증 동작 확인
- [ ] SSE 실시간 대시보드 동작 확인
- [ ] 메뉴 CRUD API 동작 확인
- [ ] 주문 상태 변경 API 동작 확인

### Phase 3 완료 조건
- [ ] 전체 API 테스트 통과
- [ ] 에러 핸들링 완료
- [ ] API 문서 완성
- [ ] Frontend/MCP 연동 준비 완료

---

## API Endpoints Summary

### Customer API (`/api/customer/*`)
```
POST   /api/customer/auth/login              # 테이블 로그인
GET    /api/customer/categories              # 카테고리 목록
GET    /api/customer/menus                   # 메뉴 목록 (query: category_id, serving_size)
GET    /api/customer/menus/{id}              # 메뉴 상세
GET    /api/customer/menus/{id}/image        # 메뉴 이미지
POST   /api/customer/orders                  # 주문 생성
GET    /api/customer/orders                  # 주문 내역 (query: session_id)
GET    /api/customer/orders/{id}             # 주문 상세
POST   /api/customer/staff-call              # 직원 호출
```

### Admin API (`/api/admin/*`)
```
POST   /api/admin/auth/login                 # 관리자 로그인
POST   /api/admin/auth/logout                # 로그아웃
GET    /api/admin/orders                     # 현재 주문 목록 (query: table_id)
GET    /api/admin/orders/{id}                # 주문 상세
PATCH  /api/admin/orders/{id}/status         # 주문 상태 변경
DELETE /api/admin/orders/{id}                # 주문 삭제
GET    /api/admin/orders/history             # 과거 주문 (query: date_from, date_to, table_id)
GET    /api/admin/tables                     # 테이블 목록
GET    /api/admin/tables/{id}                # 테이블 상세
POST   /api/admin/tables/{id}/complete       # 테이블 이용 완료
GET    /api/admin/tables/{id}/summary        # 테이블 요약
GET    /api/admin/menus                      # 메뉴 목록 (query: category_id)
POST   /api/admin/menus                      # 메뉴 등록
PUT    /api/admin/menus/{id}                 # 메뉴 수정
DELETE /api/admin/menus/{id}                 # 메뉴 삭제
POST   /api/admin/menus/{id}/image           # 메뉴 이미지 업로드
PATCH  /api/admin/menus/order                # 메뉴 순서 변경
GET    /api/admin/categories                 # 카테고리 목록
POST   /api/admin/categories                 # 카테고리 등록
PUT    /api/admin/categories/{id}            # 카테고리 수정
DELETE /api/admin/categories/{id}            # 카테고리 삭제
GET    /api/admin/staff-calls                # 직원 호출 목록 (query: acknowledged)
PATCH  /api/admin/staff-calls/{id}/acknowledge  # 호출 확인
```

### SSE API (`/api/sse/*`)
```
GET    /api/sse/orders                       # 관리자용 주문 스트림
GET    /api/sse/order-status/{table_id}      # 고객용 상태 스트림
GET    /api/sse/staff-calls                  # 관리자용 호출 스트림
```

---

## Notes
- Mock API와 동일한 스펙 유지
- OpenAPI 스펙 (`/docs/openapi.yaml`)과 일치하도록 구현
- Phase 1 완료 후 Frontend/MCP가 실제 API로 전환 가능
