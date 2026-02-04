# Component Methods (API Endpoints)

## 1. Customer API (`/api/customer/*`)

### 1.1 Authentication
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| POST | `/auth/login` | 테이블 로그인 | `{ store_code, table_number, password }` | `{ token, table_id, session_id }` |

### 1.2 Categories
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| GET | `/categories` | 카테고리 목록 | - | `[Category]` |

### 1.3 Menus
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| GET | `/menus` | 메뉴 목록 | `?category_id=&serving_size=` | `[Menu]` |
| GET | `/menus/{id}` | 메뉴 상세 | - | `Menu` |
| GET | `/menus/{id}/image` | 메뉴 이미지 | - | `image/jpeg` |

### 1.4 Cart
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| GET | `/cart` | 장바구니 조회 | `?session_id=` | `Cart` |
| POST | `/cart` | 장바구니 추가 | `{ session_id, menu_id, quantity, options? }` | `Cart` |
| DELETE | `/cart` | 장바구니 비우기 | `?session_id=` | `{ success }` |
| PATCH | `/cart/{item_id}` | 수량 변경 | `{ quantity }` | `Cart` |
| DELETE | `/cart/{item_id}` | 항목 삭제 | - | `Cart` |

### 1.5 Orders
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| POST | `/orders` | 주문 생성 | `{ session_id, items: [{menu_id, quantity}] }` | `{ order_id, order_number }` |
| GET | `/orders` | 주문 내역 | `?session_id=` | `[Order]` |
| GET | `/orders/{id}` | 주문 상세 | - | `Order` |

### 1.6 Staff Call
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| POST | `/staff-call` | 직원 호출 | `{ table_id }` | `{ success, call_id }` |

---

## 2. Admin API (`/api/admin/*`)

### 2.1 Authentication
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| POST | `/auth/login` | 관리자 로그인 | `{ store_code, username, password }` | `{ token, store_id, user_id }` |
| POST | `/auth/logout` | 로그아웃 | - | `{ success }` |

### 2.2 Orders
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| GET | `/orders` | 현재 주문 목록 | `?table_id=` | `[Order]` |
| GET | `/orders/{id}` | 주문 상세 | - | `Order` |
| PATCH | `/orders/{id}/status` | 상태 변경 | `{ status }` | `{ success }` |
| DELETE | `/orders/{id}` | 주문 삭제 | - | `{ success }` |
| GET | `/orders/history` | 과거 주문 | `?date_from=&date_to=&table_id=` | `[Order]` |

### 2.3 Tables
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| GET | `/tables` | 테이블 목록 | - | `[Table]` |
| GET | `/tables/{id}` | 테이블 상세 | - | `Table` |
| POST | `/tables/{id}/complete` | 이용 완료 | - | `{ success }` |
| GET | `/tables/{id}/summary` | 테이블 요약 | - | `{ total_amount, order_count }` |

### 2.4 Menus
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| GET | `/menus` | 메뉴 목록 | `?category_id=` | `[Menu]` |
| POST | `/menus` | 메뉴 등록 | `MenuCreate` | `Menu` |
| PUT | `/menus/{id}` | 메뉴 수정 | `MenuUpdate` | `Menu` |
| DELETE | `/menus/{id}` | 메뉴 삭제 | - | `{ success }` |
| POST | `/menus/{id}/image` | 이미지 업로드 | `multipart/form-data` | `{ success }` |
| PATCH | `/menus/order` | 순서 변경 | `[{ id, display_order }]` | `{ success }` |

### 2.5 Categories
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| GET | `/categories` | 카테고리 목록 | - | `[Category]` |
| POST | `/categories` | 카테고리 등록 | `CategoryCreate` | `Category` |
| PUT | `/categories/{id}` | 카테고리 수정 | `CategoryUpdate` | `Category` |
| DELETE | `/categories/{id}` | 카테고리 삭제 | - | `{ success }` |

### 2.6 Staff Calls
| Method | Endpoint | Description | Request | Response |
|--------|----------|-------------|---------|----------|
| GET | `/staff-calls` | 호출 목록 | `?acknowledged=` | `[StaffCall]` |
| PATCH | `/staff-calls/{id}/acknowledge` | 호출 확인 | - | `{ success }` |

---

## 3. SSE API (`/api/sse/*`)

| Method | Endpoint | Description | Events |
|--------|----------|-------------|--------|
| GET | `/orders` | 관리자용 주문 스트림 | `new_order`, `order_status_changed`, `order_deleted` |
| GET | `/order-status/{table_id}` | 고객용 상태 스트림 | `order_status_changed` |
| GET | `/staff-calls` | 관리자용 호출 스트림 | `staff_call`, `staff_call_acknowledged` |

---

## 4. Customer MCP Tools

### 4.1 Context Setup (필수 최초 호출)
| Tool | Parameters | Returns | Description |
|------|------------|---------|-------------|
| `set_table_context` | `store_code, table_number, password` | `{ success, table_id, session_id }` | 테이블 컨텍스트 설정 (필수) |
| `get_table_info` | - | `{ table_number, store_name, session_id }` | 현재 테이블 정보 |

### 4.2 Menu & Cart (table_context 필수)
| Tool | Parameters | Returns |
|------|------------|---------|
| `get_menu_list` | `category_id?, serving_size?` | `[Menu]` |
| `get_menu_detail` | `menu_id` | `Menu` |
| `add_to_cart` | `menu_id, quantity` | `Cart` |
| `update_cart_item` | `menu_id, quantity` | `Cart` |
| `remove_from_cart` | `menu_id` | `Cart` |
| `get_cart` | - | `Cart` |
| `clear_cart` | - | `{ success }` |

### 4.3 Order (table_context 필수)
| Tool | Parameters | Returns |
|------|------------|---------|
| `create_order` | - | `Order` |
| `get_order_history` | - | `[Order]` |
| `get_order_status` | `order_id` | `Order` |
| `call_staff` | - | `{ success }` |

---

## 5. Admin MCP Tools

### 5.1 Context Setup (필수 최초 호출)
| Tool | Parameters | Returns | Description |
|------|------------|---------|-------------|
| `set_admin_context` | `store_code, username, password` | `{ success, store_id, token }` | 관리자 컨텍스트 설정 (필수) |

### 5.2 Order Management (admin_context 필수)
| Tool | Parameters | Returns |
|------|------------|---------|
| `get_orders` | `table_id?` | `[Order]` |
| `get_order_detail` | `order_id` | `Order` |
| `update_order_status` | `order_id, status` | `{ success }` |
| `delete_order` | `order_id` | `{ success }` |
| `complete_table_session` | `table_id` | `{ success }` |
| `get_order_history` | `date_from?, date_to?, table_id?` | `[Order]` |

### 5.3 Menu Management (admin_context 필수)
| Tool | Parameters | Returns |
|------|------------|---------|
| `get_menus` | `category_id?` | `[Menu]` |
| `create_menu` | `MenuCreate` | `Menu` |
| `update_menu` | `menu_id, MenuUpdate` | `Menu` |
| `delete_menu` | `menu_id` | `{ success }` |
| `get_staff_calls` | `acknowledged?` | `[StaffCall]` |
