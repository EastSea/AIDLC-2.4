# Contract/Interface Definition for Unit 2 (Frontend)

## Unit Context
- **Stories**: US-1.2, US-2.1, US-2.2, US-2.3, US-3.1, US-3.2, US-3.3, US-4.1, US-4.2, US-5.1, US-5.2, US-6.1, US-6.2, US-6.3, US-7.1, US-8.1, US-8.2, US-8.3, US-9.1, US-9.2, US-9.3, US-10.1~10.5
- **Dependencies**: Mock API (localhost:8001), OpenAPI spec
- **Technology**: React 18, React Router 6, Axios

---

## API Service Layer

### `apiClient.js`
Base axios configuration for API calls

- `createApiClient() -> AxiosInstance`: Create configured axios instance
  - Returns: Axios instance with base URL and interceptors

### `authService.js`
Customer and admin authentication

- `loginTable(storeCode, tableNumber, password) -> Promise<{token, tableId, sessionId}>`: Customer table login
  - Args: storeCode (string), tableNumber (number), password (string)
  - Returns: Promise resolving to auth response
  - Raises: API error on invalid credentials

- `loginAdmin(storeCode, username, password) -> Promise<{token, storeId, userId}>`: Admin login
  - Args: storeCode (string), username (string), password (string)
  - Returns: Promise resolving to admin auth response
  - Raises: API error on invalid credentials

### `menuService.js`
Menu browsing and filtering

- `getCategories() -> Promise<Category[]>`: Fetch all categories
  - Returns: Promise resolving to category array
  
- `getMenus(categoryId?, servingSize?) -> Promise<Menu[]>`: Fetch menus with filters
  - Args: categoryId (string, optional), servingSize (string, optional)
  - Returns: Promise resolving to menu array
  
- `getMenuDetail(menuId) -> Promise<Menu>`: Fetch menu details
  - Args: menuId (string)
  - Returns: Promise resolving to menu object

### `orderService.js`
Order creation and history

- `createOrder(sessionId, items) -> Promise<{orderId, orderNumber}>`: Create new order
  - Args: sessionId (string), items (array of {menuId, quantity})
  - Returns: Promise resolving to order response
  - Raises: API error on order failure

- `getOrders(sessionId) -> Promise<Order[]>`: Fetch order history
  - Args: sessionId (string)
  - Returns: Promise resolving to order array

### `staffService.js`
Staff call functionality

- `callStaff(tableId) -> Promise<{success, callId}>`: Call staff to table
  - Args: tableId (string)
  - Returns: Promise resolving to call response

### `adminOrderService.js`
Admin order management

- `getAdminOrders(tableId?) -> Promise<Order[]>`: Fetch orders for admin
  - Args: tableId (string, optional)
  - Returns: Promise resolving to order array

- `updateOrderStatus(orderId, status) -> Promise<{success}>`: Update order status
  - Args: orderId (string), status (string: pending|preparing|completed)
  - Returns: Promise resolving to success response

- `deleteOrder(orderId) -> Promise<{success}>`: Delete order
  - Args: orderId (string)
  - Returns: Promise resolving to success response

### `adminTableService.js`
Admin table management

- `completeTable(tableId) -> Promise<{success}>`: Mark table as completed
  - Args: tableId (string)
  - Returns: Promise resolving to success response

### `adminMenuService.js`
Admin menu CRUD

- `getAdminMenus() -> Promise<Menu[]>`: Fetch all menus for admin
  - Returns: Promise resolving to menu array

- `createMenu(menuData) -> Promise<Menu>`: Create new menu
  - Args: menuData (object with categoryId, name, price, description, servingSize)
  - Returns: Promise resolving to created menu

- `updateMenu(menuId, menuData) -> Promise<Menu>`: Update menu
  - Args: menuId (string), menuData (object)
  - Returns: Promise resolving to updated menu

- `deleteMenu(menuId) -> Promise<{success}>`: Delete menu
  - Args: menuId (string)
  - Returns: Promise resolving to success response

### `sseService.js`
Server-Sent Events for real-time updates

- `subscribeOrderStatus(tableId, onMessage) -> EventSource`: Subscribe to order status updates
  - Args: tableId (string), onMessage (callback function)
  - Returns: EventSource instance

- `subscribeAdminOrders(token, onMessage) -> EventSource`: Subscribe to admin order updates
  - Args: token (string), onMessage (callback function)
  - Returns: EventSource instance

---

## Custom Hooks Layer

### `useAuth.js`
Authentication state management

- `useAuth() -> {isAuthenticated, user, login, logout}`: Auth hook
  - Returns: Auth state and methods

### `useCart.js`
Shopping cart state management

- `useCart() -> {items, addItem, removeItem, updateQuantity, clearCart, totalAmount}`: Cart hook
  - Returns: Cart state and methods

### `useOrders.js`
Order history management

- `useOrders(sessionId) -> {orders, loading, error, refetch}`: Orders hook
  - Args: sessionId (string)
  - Returns: Orders state and methods

### `useSSE.js`
SSE connection management

- `useSSE(url, onMessage) -> {connected, error}`: SSE hook
  - Args: url (string), onMessage (callback)
  - Returns: Connection state

### `useIdleTimeout.js`
Idle timeout detection

- `useIdleTimeout(timeoutMs, onTimeout) -> void`: Idle timeout hook
  - Args: timeoutMs (number), onTimeout (callback)

---

## Component Layer

### Customer Components

#### `CustomerLogin.jsx`
- Props: None
- State: storeCode, tableNumber, password, error
- Methods: handleLogin()

#### `MenuBrowser.jsx`
- Props: None
- State: selectedCategory, servingSize, menus, loading
- Methods: handleCategoryChange(), handleFilterChange()

#### `MenuCard.jsx`
- Props: menu (object), onAddToCart (function)
- Methods: handleAddToCart()

#### `MenuDetail.jsx`
- Props: menuId (string)
- State: menu, loading
- Methods: handleAddToCart()

#### `Cart.jsx`
- Props: None
- State: items (from useCart)
- Methods: handleUpdateQuantity(), handleRemove(), handleCheckout()

#### `OrderHistory.jsx`
- Props: sessionId (string)
- State: orders, loading
- Methods: None (display only)

#### `StaffCallButton.jsx`
- Props: tableId (string)
- Methods: handleCallStaff()

### Admin Components

#### `AdminLogin.jsx`
- Props: None
- State: storeCode, username, password, error
- Methods: handleLogin()

#### `AdminDashboard.jsx`
- Props: None
- State: orders, loading
- Methods: handleStatusChange(), handleDelete()

#### `OrderCard.jsx`
- Props: order (object), onStatusChange (function), onDelete (function)
- Methods: handleStatusChange(), handleDelete()

#### `MenuManagement.jsx`
- Props: None
- State: menus, loading, editingMenu
- Methods: handleCreate(), handleUpdate(), handleDelete()

#### `MenuForm.jsx`
- Props: menu (object, optional), onSubmit (function), onCancel (function)
- State: formData
- Methods: handleSubmit()

---

## Routing Structure

### `App.js`
Main application router

Routes:
- `/` - Customer menu browser (default)
- `/menu/:menuId` - Menu detail
- `/cart` - Shopping cart
- `/orders` - Order history
- `/admin/login` - Admin login
- `/admin/dashboard` - Admin dashboard
- `/admin/menus` - Menu management

---

## Local Storage Schema

### Customer Auth
```javascript
{
  "tableAuth": {
    "token": "string",
    "tableId": "string",
    "sessionId": "string",
    "tableNumber": number
  }
}
```

### Cart
```javascript
{
  "cart": [
    {
      "menuId": "string",
      "name": "string",
      "price": number,
      "quantity": number
    }
  ]
}
```

### Admin Auth
```javascript
{
  "adminAuth": {
    "token": "string",
    "storeId": "string",
    "userId": "string"
  }
}
```
