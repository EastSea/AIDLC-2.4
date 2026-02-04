# Entity-Model-Table Mapping

## Overview
Frontend Entity → Backend Model (Pydantic Schema + SQLAlchemy) → Database Table 일관된 매핑

---

## 1. Store (매장)

### Frontend Entity
```typescript
interface Store {
  id: string;
  name: string;
  code: string;  // 매장 식별 코드
}
```

### Backend Pydantic Schema
```python
class StoreBase(BaseModel):
    name: str
    code: str

class StoreResponse(StoreBase):
    id: UUID
```

### Backend SQLAlchemy Model
```python
class Store(Base):
    __tablename__ = "stores"
    id: UUID
    name: str
    code: str  # unique
    created_at: datetime
```

### Database Table
```sql
CREATE TABLE stores (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    code VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 2. AdminUser (관리자)

### Frontend Entity
```typescript
interface AdminUser {
  id: string;
  storeId: string;
  username: string;
}
```

### Backend Pydantic Schema
```python
class AdminUserCreate(BaseModel):
    store_id: UUID
    username: str
    password: str

class AdminUserResponse(BaseModel):
    id: UUID
    store_id: UUID
    username: str
```

### Backend SQLAlchemy Model
```python
class AdminUser(Base):
    __tablename__ = "admin_users"
    id: UUID
    store_id: UUID  # FK -> stores.id
    username: str
    password_hash: str  # bcrypt
    created_at: datetime
```

### Database Table
```sql
CREATE TABLE admin_users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    store_id UUID NOT NULL REFERENCES stores(id),
    username VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(store_id, username)
);
```

---

## 3. Table (테이블)

### Frontend Entity
```typescript
interface Table {
  id: string;
  storeId: string;
  tableNumber: number;
}
```

### Backend Pydantic Schema
```python
class TableCreate(BaseModel):
    store_id: UUID
    table_number: int
    password: str

class TableResponse(BaseModel):
    id: UUID
    store_id: UUID
    table_number: int
```

### Backend SQLAlchemy Model
```python
class Table(Base):
    __tablename__ = "tables"
    id: UUID
    store_id: UUID  # FK -> stores.id
    table_number: int
    password_hash: str
    created_at: datetime
```

### Database Table
```sql
CREATE TABLE tables (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    store_id UUID NOT NULL REFERENCES stores(id),
    table_number INT NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(store_id, table_number)
);
```

---

## 4. TableSession (테이블 세션)

### Frontend Entity
```typescript
interface TableSession {
  id: string;
  tableId: string;
  startedAt: string;
  endedAt?: string;
  isActive: boolean;
}
```

### Backend Pydantic Schema
```python
class TableSessionResponse(BaseModel):
    id: UUID
    table_id: UUID
    started_at: datetime
    ended_at: Optional[datetime]
    is_active: bool
```

### Backend SQLAlchemy Model
```python
class TableSession(Base):
    __tablename__ = "table_sessions"
    id: UUID
    table_id: UUID  # FK -> tables.id
    started_at: datetime
    ended_at: Optional[datetime]
    is_active: bool
```

### Database Table
```sql
CREATE TABLE table_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    table_id UUID NOT NULL REFERENCES tables(id),
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ended_at TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);
```

---

## 5. Category (카테고리)

### Frontend Entity
```typescript
interface Category {
  id: string;
  storeId: string;
  name: string;
  displayOrder: number;
}
```

### Backend Pydantic Schema
```python
class CategoryCreate(BaseModel):
    store_id: UUID
    name: str
    display_order: int = 0

class CategoryResponse(CategoryCreate):
    id: UUID
```

### Backend SQLAlchemy Model
```python
class Category(Base):
    __tablename__ = "categories"
    id: UUID
    store_id: UUID  # FK -> stores.id
    name: str
    display_order: int
```

### Database Table
```sql
CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    store_id UUID NOT NULL REFERENCES stores(id),
    name VARCHAR(50) NOT NULL,
    display_order INT DEFAULT 0
);
```

---

## 6. Menu (메뉴)

### Frontend Entity
```typescript
interface Menu {
  id: string;
  categoryId: string;
  name: string;
  price: number;
  description?: string;
  imageUrl?: string;
  servingSize: string;  // "1-2", "3-4", "all"
  displayOrder: number;
  isAvailable: boolean;
}
```

### Backend Pydantic Schema
```python
class MenuCreate(BaseModel):
    category_id: UUID
    name: str
    price: int
    description: Optional[str]
    serving_size: str  # "1-2", "3-4", "all"
    display_order: int = 0
    is_available: bool = True

class MenuResponse(MenuCreate):
    id: UUID
    image_url: Optional[str]
```

### Backend SQLAlchemy Model
```python
class Menu(Base):
    __tablename__ = "menus"
    id: UUID
    category_id: UUID  # FK -> categories.id
    name: str
    price: int
    description: Optional[str]
    serving_size: str
    display_order: int
    is_available: bool
    created_at: datetime
```

### Database Table
```sql
CREATE TABLE menus (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category_id UUID NOT NULL REFERENCES categories(id),
    name VARCHAR(100) NOT NULL,
    price INT NOT NULL,
    description TEXT,
    serving_size VARCHAR(10) DEFAULT 'all',
    display_order INT DEFAULT 0,
    is_available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 7. MenuImage (메뉴 이미지)

### Frontend Entity
```typescript
interface MenuImage {
  menuId: string;
  imageData: string;  // base64 or URL
  contentType: string;
}
```

### Backend Pydantic Schema
```python
class MenuImageCreate(BaseModel):
    menu_id: UUID
    content_type: str

class MenuImageResponse(BaseModel):
    menu_id: UUID
    content_type: str
    image_url: str  # /api/customer/menus/{id}/image
```

### Backend SQLAlchemy Model
```python
class MenuImage(Base):
    __tablename__ = "menu_images"
    menu_id: UUID  # PK, FK -> menus.id
    image_data: bytes  # BYTEA
    content_type: str
```

### Database Table
```sql
CREATE TABLE menu_images (
    menu_id UUID PRIMARY KEY REFERENCES menus(id) ON DELETE CASCADE,
    image_data BYTEA NOT NULL,
    content_type VARCHAR(50) NOT NULL
);
```

---

## 8. Order (주문)

### Frontend Entity
```typescript
interface Order {
  id: string;
  sessionId: string;
  orderNumber: string;
  status: 'pending' | 'preparing' | 'completed';
  totalAmount: number;
  createdAt: string;
  items: OrderItem[];
}
```

### Backend Pydantic Schema
```python
class OrderCreate(BaseModel):
    session_id: UUID
    items: List[OrderItemCreate]

class OrderResponse(BaseModel):
    id: UUID
    session_id: UUID
    order_number: str
    status: str  # pending, preparing, completed
    total_amount: int
    created_at: datetime
    items: List[OrderItemResponse]
```

### Backend SQLAlchemy Model
```python
class Order(Base):
    __tablename__ = "orders"
    id: UUID
    session_id: UUID  # FK -> table_sessions.id
    order_number: str  # 표시용 주문번호
    status: str  # pending, preparing, completed
    total_amount: int
    created_at: datetime
```

### Database Table
```sql
CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES table_sessions(id),
    order_number VARCHAR(20) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    total_amount INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 9. OrderItem (주문 항목)

### Frontend Entity
```typescript
interface OrderItem {
  id: string;
  orderId: string;
  menuId: string;
  menuName: string;
  quantity: number;
  unitPrice: number;
  subtotal: number;
}
```

### Backend Pydantic Schema
```python
class OrderItemCreate(BaseModel):
    menu_id: UUID
    quantity: int

class OrderItemResponse(BaseModel):
    id: UUID
    order_id: UUID
    menu_id: UUID
    menu_name: str
    quantity: int
    unit_price: int
    subtotal: int
```

### Backend SQLAlchemy Model
```python
class OrderItem(Base):
    __tablename__ = "order_items"
    id: UUID
    order_id: UUID  # FK -> orders.id
    menu_id: UUID  # FK -> menus.id
    menu_name: str  # 주문 시점 메뉴명 스냅샷
    quantity: int
    unit_price: int  # 주문 시점 가격 스냅샷
    subtotal: int
```

### Database Table
```sql
CREATE TABLE order_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id UUID NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    menu_id UUID NOT NULL REFERENCES menus(id),
    menu_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    unit_price INT NOT NULL,
    subtotal INT NOT NULL
);
```

---

## 10. StaffCall (직원 호출)

### Frontend Entity
```typescript
interface StaffCall {
  id: string;
  tableId: string;
  tableNumber: number;
  createdAt: string;
  acknowledged: boolean;
}
```

### Backend Pydantic Schema
```python
class StaffCallCreate(BaseModel):
    table_id: UUID

class StaffCallResponse(BaseModel):
    id: UUID
    table_id: UUID
    table_number: int
    created_at: datetime
    acknowledged: bool
```

### Backend SQLAlchemy Model
```python
class StaffCall(Base):
    __tablename__ = "staff_calls"
    id: UUID
    table_id: UUID  # FK -> tables.id
    created_at: datetime
    acknowledged: bool
    acknowledged_at: Optional[datetime]
```

### Database Table
```sql
CREATE TABLE staff_calls (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    table_id UUID NOT NULL REFERENCES tables(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    acknowledged BOOLEAN DEFAULT FALSE,
    acknowledged_at TIMESTAMP
);
```

---

## Entity Relationship Diagram

```
stores
  |
  +-- admin_users (1:N)
  |
  +-- tables (1:N)
  |     |
  |     +-- table_sessions (1:N)
  |     |     |
  |     |     +-- orders (1:N)
  |     |           |
  |     |           +-- order_items (1:N)
  |     |
  |     +-- staff_calls (1:N)
  |
  +-- categories (1:N)
        |
        +-- menus (1:N)
              |
              +-- menu_images (1:1)
```
