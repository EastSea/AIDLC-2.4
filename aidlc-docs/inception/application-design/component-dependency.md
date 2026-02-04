# Component Dependencies

## Dependency Matrix

| Component | Depends On |
|-----------|------------|
| **Frontend (React)** | Backend API |
| **Customer MCP Server** | Backend API |
| **Admin MCP Server** | Backend API |
| **Backend API** | PostgreSQL, SSE |
| **PostgreSQL** | - |

---

## Layer Dependencies

```
+------------------------------------------------------------------+
|                         PRESENTATION LAYER                        |
+------------------------------------------------------------------+
|  +----------------+  +----------------+  +--------------------+   |
|  | Customer Web   |  | Admin Web      |  | MCP Servers        |   |
|  | (React)        |  | (React)        |  | (Python)           |   |
|  +----------------+  +----------------+  +--------------------+   |
|         |                   |                    |                |
|         +-------------------+--------------------+                |
|                             |                                     |
|                             v                                     |
+------------------------------------------------------------------+
|                          API LAYER                                |
+------------------------------------------------------------------+
|  +----------------+  +----------------+  +--------------------+   |
|  | Customer API   |  | Admin API      |  | SSE API            |   |
|  | /api/customer  |  | /api/admin     |  | /api/sse           |   |
|  +----------------+  +----------------+  +--------------------+   |
|         |                   |                    |                |
|         +-------------------+--------------------+                |
|                             |                                     |
|                             v                                     |
+------------------------------------------------------------------+
|                        SERVICE LAYER                              |
+------------------------------------------------------------------+
|  +----------+ +----------+ +----------+ +----------+ +----------+ |
|  |AuthSvc   | |MenuSvc   | |OrderSvc  | |TableSvc  | |SSESvc    | |
|  +----------+ +----------+ +----------+ +----------+ +----------+ |
|         |           |           |            |            |       |
|         +-----------+-----------+------------+------------+       |
|                             |                                     |
|                             v                                     |
+------------------------------------------------------------------+
|                      REPOSITORY LAYER                             |
+------------------------------------------------------------------+
|  +----------+ +----------+ +----------+ +----------+ +----------+ |
|  |TableRepo | |MenuRepo  | |OrderRepo | |SessionRp | |ImageRepo | |
|  +----------+ +----------+ +----------+ +----------+ +----------+ |
|         |           |           |            |            |       |
|         +-----------+-----------+------------+------------+       |
|                             |                                     |
|                             v                                     |
+------------------------------------------------------------------+
|                         DATA LAYER                                |
+------------------------------------------------------------------+
|                      +----------------+                           |
|                      |   PostgreSQL   |                           |
|                      +----------------+                           |
+------------------------------------------------------------------+
```

---

## Frontend → Backend Communication

### Customer Web
| Action | API Call | Response |
|--------|----------|----------|
| 로그인 | POST /api/customer/auth/login | JWT Token |
| 메뉴 조회 | GET /api/customer/menus | [Menu] |
| 주문 생성 | POST /api/customer/orders | Order |
| 주문 상태 구독 | GET /api/sse/order-status/{table_id} | SSE Stream |

### Admin Web
| Action | API Call | Response |
|--------|----------|----------|
| 로그인 | POST /api/admin/auth/login | JWT Token |
| 주문 조회 | GET /api/admin/orders | [Order] |
| 상태 변경 | PATCH /api/admin/orders/{id}/status | Success |
| 주문 구독 | GET /api/sse/orders | SSE Stream |

---

## MCP Server → Backend Communication

### Customer MCP Server
```
+------------------+       +------------------+
| Customer MCP     |       | Backend API      |
| Server           |------>| /api/customer/*  |
+------------------+       +------------------+
        |
        | HTTP Client (httpx/requests)
        |
        v
  Uses same endpoints as Customer Web
```

### Admin MCP Server
```
+------------------+       +------------------+
| Admin MCP        |       | Backend API      |
| Server           |------>| /api/admin/*     |
+------------------+       +------------------+
        |
        | HTTP Client (httpx/requests)
        |
        v
  Uses same endpoints as Admin Web
```

---

## Data Flow

### 주문 생성 Data Flow
```
Customer Web                Backend                    Database
     |                         |                          |
     | 1. POST /orders         |                          |
     |------------------------>|                          |
     |                         | 2. Validate session      |
     |                         |------------------------->|
     |                         |<-------------------------|
     |                         |                          |
     |                         | 3. Get menu prices       |
     |                         |------------------------->|
     |                         |<-------------------------|
     |                         |                          |
     |                         | 4. Insert order          |
     |                         |------------------------->|
     |                         |<-------------------------|
     |                         |                          |
     |                         | 5. Insert order_items    |
     |                         |------------------------->|
     |                         |<-------------------------|
     |                         |                          |
     | 6. Order response       |                          |
     |<------------------------|                          |
     |                         |                          |
     |                         | 7. SSE broadcast         |
     |                         |----------+               |
     |                         |          | (to Admin)    |
     |                         |<---------+               |
```

### SSE Event Flow
```
+----------+       +----------+       +----------+
| Customer |       | Backend  |       |  Admin   |
|   Web    |       |   API    |       |   Web    |
+----------+       +----------+       +----------+
     |                  |                  |
     |                  |<----- SSE -------|
     |                  |   Connection     |
     |                  |                  |
     | POST /orders     |                  |
     |----------------->|                  |
     |                  |                  |
     |                  |--- new_order --->|
     |                  |   (SSE Event)    |
     |                  |                  |
     |                  |                  |
     |                  | PATCH /status    |
     |                  |<-----------------|
     |                  |                  |
     |<-- status_changed                   |
     |   (SSE Event)    |                  |
```

---

## External Dependencies

| Dependency | Purpose | Version |
|------------|---------|---------|
| FastAPI | Web Framework | ^0.100 |
| SQLAlchemy | ORM | ^2.0 |
| Alembic | DB Migration | ^1.12 |
| Pydantic | Data Validation | ^2.0 |
| python-jose | JWT | ^3.3 |
| passlib[bcrypt] | Password Hashing | ^1.7 |
| asyncpg | PostgreSQL Driver | ^0.28 |
| sse-starlette | SSE Support | ^1.6 |
| React | Frontend Framework | ^18 |
| React Router | Routing | ^6 |
| Axios | HTTP Client | ^1.5 |
| mcp | MCP SDK | latest |
