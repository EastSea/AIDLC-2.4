# Services Definition

## Backend Services Layer

```
+------------------+     +------------------+     +------------------+
|     Routers      |---->|     Services     |---->|   Repositories   |
+------------------+     +------------------+     +------------------+
                                  |
                                  v
                         +------------------+
                         |   External Deps  |
                         | (SSE, JWT, etc.) |
                         +------------------+
```

---

## 1. AuthService

### Responsibility
- JWT 토큰 발급 및 검증
- 테이블 로그인 처리
- 관리자 로그인 처리
- 세션 관리

### Methods
| Method | Description |
|--------|-------------|
| `login_table(store_code, table_number, password)` | 테이블 로그인, 세션 생성/조회 |
| `login_admin(store_code, username, password)` | 관리자 로그인 |
| `verify_token(token)` | JWT 토큰 검증 |
| `create_token(payload, expires_delta)` | JWT 토큰 생성 |
| `hash_password(password)` | bcrypt 해싱 |
| `verify_password(plain, hashed)` | 비밀번호 검증 |

### Dependencies
- `TableRepository`
- `AdminUserRepository`
- `TableSessionRepository`

---

## 2. MenuService

### Responsibility
- 메뉴 CRUD
- 카테고리 관리
- 이미지 관리
- 메뉴 순서 관리

### Methods
| Method | Description |
|--------|-------------|
| `get_categories(store_id)` | 카테고리 목록 조회 |
| `get_menus(store_id, category_id?, serving_size?)` | 메뉴 목록 조회 |
| `get_menu(menu_id)` | 메뉴 상세 조회 |
| `create_menu(menu_data)` | 메뉴 등록 |
| `update_menu(menu_id, menu_data)` | 메뉴 수정 |
| `delete_menu(menu_id)` | 메뉴 삭제 |
| `update_menu_order(menu_orders)` | 메뉴 순서 변경 |
| `upload_image(menu_id, image_data)` | 이미지 업로드 |
| `get_image(menu_id)` | 이미지 조회 |

### Dependencies
- `MenuRepository`
- `CategoryRepository`
- `MenuImageRepository`

---

## 3. OrderService

### Responsibility
- 주문 생성
- 주문 상태 관리
- 주문 조회
- 주문 삭제

### Methods
| Method | Description |
|--------|-------------|
| `create_order(session_id, items)` | 주문 생성 |
| `get_orders(session_id?, table_id?, status?)` | 주문 목록 조회 |
| `get_order(order_id)` | 주문 상세 조회 |
| `update_status(order_id, status)` | 주문 상태 변경 |
| `delete_order(order_id)` | 주문 삭제 |
| `get_order_history(store_id, date_from?, date_to?, table_id?)` | 과거 주문 조회 |
| `generate_order_number()` | 주문번호 생성 |

### Dependencies
- `OrderRepository`
- `OrderItemRepository`
- `MenuRepository`
- `SSEService`

---

## 4. TableService

### Responsibility
- 테이블 세션 관리
- 이용 완료 처리
- 테이블 요약 정보

### Methods
| Method | Description |
|--------|-------------|
| `get_tables(store_id)` | 테이블 목록 조회 |
| `get_table(table_id)` | 테이블 상세 조회 |
| `get_or_create_session(table_id)` | 세션 조회 또는 생성 |
| `complete_session(table_id)` | 이용 완료 처리 |
| `get_table_summary(table_id)` | 테이블 요약 (총액, 주문수) |

### Dependencies
- `TableRepository`
- `TableSessionRepository`
- `OrderRepository`
- `SSEService`

---

## 5. SSEService

### Responsibility
- 실시간 이벤트 브로드캐스트
- 클라이언트 연결 관리
- 이벤트 타입별 라우팅

### Methods
| Method | Description |
|--------|-------------|
| `connect(client_id, event_types)` | 클라이언트 연결 |
| `disconnect(client_id)` | 클라이언트 연결 해제 |
| `broadcast(event_type, data, filter?)` | 이벤트 브로드캐스트 |
| `send_to_client(client_id, event_type, data)` | 특정 클라이언트에 전송 |

### Event Types
| Event | Description | Target |
|-------|-------------|--------|
| `new_order` | 새 주문 발생 | Admin |
| `order_status_changed` | 주문 상태 변경 | Admin, Customer |
| `order_deleted` | 주문 삭제 | Admin |
| `table_completed` | 테이블 이용 완료 | Admin |
| `staff_call` | 직원 호출 | Admin |
| `staff_call_acknowledged` | 호출 확인 | Admin |

### Dependencies
- None (독립적)

---

## 6. StaffCallService

### Responsibility
- 직원 호출 생성
- 호출 목록 조회
- 호출 확인 처리

### Methods
| Method | Description |
|--------|-------------|
| `create_call(table_id)` | 직원 호출 생성 |
| `get_calls(store_id, acknowledged?)` | 호출 목록 조회 |
| `acknowledge_call(call_id)` | 호출 확인 처리 |

### Dependencies
- `StaffCallRepository`
- `SSEService`

---

## 7. ImageService

### Responsibility
- 이미지 업로드
- 이미지 저장 (PostgreSQL BYTEA)
- 이미지 조회

### Methods
| Method | Description |
|--------|-------------|
| `upload(menu_id, file_data, content_type)` | 이미지 업로드 |
| `get(menu_id)` | 이미지 조회 |
| `delete(menu_id)` | 이미지 삭제 |

### Dependencies
- `MenuImageRepository`

---

## Service Interaction Diagram

```
                    +-------------+
                    | AuthService |
                    +-------------+
                          |
          +---------------+---------------+
          |               |               |
          v               v               v
    +-----------+   +-----------+   +-----------+
    |MenuService|   |OrderService|  |TableService|
    +-----------+   +-----------+   +-----------+
          |               |               |
          |               +-------+-------+
          |                       |
          v                       v
    +------------+          +----------+
    |ImageService|          |SSEService|
    +------------+          +----------+
                                  ^
                                  |
                          +---------------+
                          |StaffCallService|
                          +---------------+
```
