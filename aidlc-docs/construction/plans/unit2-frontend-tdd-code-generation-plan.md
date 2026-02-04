# TDD Code Generation Plan for Unit 2 (Frontend)

## Unit Context
- **Workspace Root**: /Users/leehyeji/dev/Projects/aidlc-workflows/AIDLC-2.4
- **Project Type**: Greenfield
- **Stories**: 24 stories (US-1.2, US-2.1~2.3, US-3.1~3.3, US-4.1~4.2, US-5.1~5.2, US-6.1~6.3, US-7.1, US-8.1~8.3, US-9.1~9.3, US-10.1~10.5)
- **Technology**: React 18, React Router 6, Axios, Jest, React Testing Library
- **Code Location**: `/web/src/`
- **Test Location**: `/web/src/__tests__/`

---

## Plan Step 0: Contract Skeleton Generation
- [x] Generate API service skeletons (`/web/src/services/`)
  - [x] apiClient.js
  - [x] authService.js
  - [x] menuService.js
  - [x] orderService.js
  - [x] staffService.js
  - [x] adminOrderService.js
  - [x] adminTableService.js
  - [x] adminMenuService.js
  - [x] sseService.js
- [x] Generate custom hooks skeletons (`/web/src/hooks/`)
  - [x] useAuth.js
  - [x] useCart.js
  - [x] useOrders.js
  - [x] useSSE.js
  - [x] useIdleTimeout.js
- [x] Generate component skeletons (`/web/src/components/`)
  - [x] customer/CustomerLogin.jsx
  - [x] customer/MenuBrowser.jsx
  - [x] customer/MenuCard.jsx
  - [x] customer/MenuDetail.jsx
  - [x] customer/Cart.jsx
  - [x] customer/OrderHistory.jsx
  - [x] customer/StaffCallButton.jsx
  - [x] admin/AdminLogin.jsx
  - [x] admin/AdminDashboard.jsx
  - [x] admin/OrderCard.jsx
  - [x] admin/MenuManagement.jsx
  - [x] admin/MenuForm.jsx
- [x] Update App.js with routing structure
- [x] Verify compilation

---

## Plan Step 1: API Service Layer (TDD)

### 1.1 apiClient.js
- [ ] createApiClient() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test (TC-FE-001 setup)
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass

### 1.2 authService.js
- [ ] loginTable() - RED-GREEN-REFACTOR (TC-FE-001, TC-FE-002)
  - [ ] RED: Write failing test for success case
  - [ ] GREEN: Minimal implementation
  - [ ] RED: Write failing test for error case
  - [ ] GREEN: Add error handling
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-1.2

- [ ] loginAdmin() - RED-GREEN-REFACTOR (TC-FE-003)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-7.1

### 1.3 menuService.js
- [ ] getCategories() - RED-GREEN-REFACTOR (TC-FE-004)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-2.1

- [ ] getMenus() - RED-GREEN-REFACTOR (TC-FE-005, TC-FE-006, TC-FE-007)
  - [ ] RED: Write failing test for no filters
  - [ ] GREEN: Minimal implementation
  - [ ] RED: Write failing test for category filter
  - [ ] GREEN: Add category filter
  - [ ] RED: Write failing test for serving size filter
  - [ ] GREEN: Add serving size filter
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-2.1, US-2.3

- [ ] getMenuDetail() - RED-GREEN-REFACTOR (TC-FE-008)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-2.2

### 1.4 orderService.js
- [ ] createOrder() - RED-GREEN-REFACTOR (TC-FE-009, TC-FE-010)
  - [ ] RED: Write failing test for success
  - [ ] GREEN: Minimal implementation
  - [ ] RED: Write failing test for error
  - [ ] GREEN: Add error handling
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-4.1, US-4.2

- [ ] getOrders() - RED-GREEN-REFACTOR (TC-FE-011)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-5.1

### 1.5 staffService.js
- [ ] callStaff() - RED-GREEN-REFACTOR (TC-FE-012)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-6.3

### 1.6 adminOrderService.js
- [ ] getAdminOrders() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-8.1

- [ ] updateOrderStatus() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-8.2

- [ ] deleteOrder() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-9.1

### 1.7 adminTableService.js
- [ ] completeTable() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-9.2

### 1.8 adminMenuService.js
- [ ] getAdminMenus() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-10.1

- [ ] createMenu() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-10.2

- [ ] updateMenu() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-10.3

- [ ] deleteMenu() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-10.4

### 1.9 sseService.js
- [ ] subscribeOrderStatus() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-5.2

- [ ] subscribeAdminOrders() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-8.1

---

## Plan Step 2: Custom Hooks Layer (TDD)

### 2.1 useCart.js
- [ ] addItem() - RED-GREEN-REFACTOR (TC-FE-013, TC-FE-014)
  - [ ] RED: Write failing test for adding new item
  - [ ] GREEN: Minimal implementation
  - [ ] RED: Write failing test for duplicate item
  - [ ] GREEN: Add quantity increment logic
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-3.1

- [ ] updateQuantity() - RED-GREEN-REFACTOR (TC-FE-015, TC-FE-016)
  - [ ] RED: Write failing test for quantity update
  - [ ] GREEN: Minimal implementation
  - [ ] RED: Write failing test for quantity 0 (remove)
  - [ ] GREEN: Add remove logic
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-3.2

- [ ] removeItem() - RED-GREEN-REFACTOR (TC-FE-017)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-3.2

- [ ] clearCart() - RED-GREEN-REFACTOR (TC-FE-018)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-4.1

- [ ] totalAmount - RED-GREEN-REFACTOR (TC-FE-019)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-3.1

- [ ] localStorage persistence - RED-GREEN-REFACTOR (TC-FE-020)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-3.3

### 2.2 useAuth.js
- [ ] login() - RED-GREEN-REFACTOR (TC-FE-021)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-1.2, US-7.1

- [ ] logout() - RED-GREEN-REFACTOR (TC-FE-022)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-7.1

### 2.3 useOrders.js
- [ ] useOrders() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-5.1

### 2.4 useSSE.js
- [ ] useSSE() - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-5.2, US-8.1

### 2.5 useIdleTimeout.js
- [ ] useIdleTimeout() - RED-GREEN-REFACTOR (TC-FE-023, TC-FE-024)
  - [ ] RED: Write failing test for timeout
  - [ ] GREEN: Minimal implementation
  - [ ] RED: Write failing test for reset
  - [ ] GREEN: Add reset logic
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-6.2

---

## Plan Step 3: Component Layer (TDD)

### 3.1 Customer Components

#### CustomerLogin.jsx
- [ ] Component rendering - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-1.2

#### MenuBrowser.jsx
- [ ] Category list rendering - RED-GREEN-REFACTOR (TC-FE-025)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-2.1

- [ ] Category filtering - RED-GREEN-REFACTOR (TC-FE-026)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-2.1

- [ ] Serving size filter - RED-GREEN-REFACTOR (TC-FE-027)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-2.3

#### MenuCard.jsx
- [ ] Menu display - RED-GREEN-REFACTOR (TC-FE-028)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-2.1

- [ ] Add to cart button - RED-GREEN-REFACTOR (TC-FE-029)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-3.1

#### MenuDetail.jsx
- [ ] Menu detail display - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-2.2

#### Cart.jsx
- [ ] Cart items display - RED-GREEN-REFACTOR (TC-FE-030)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-3.1

- [ ] Quantity controls - RED-GREEN-REFACTOR (TC-FE-031)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-3.2

- [ ] Total amount display - RED-GREEN-REFACTOR (TC-FE-032)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-3.1

- [ ] Checkout button - RED-GREEN-REFACTOR (TC-FE-033)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-4.1

#### OrderHistory.jsx
- [ ] Order list display - RED-GREEN-REFACTOR (TC-FE-034)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-5.1

- [ ] Order status display - RED-GREEN-REFACTOR (TC-FE-035)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-5.2

- [ ] SSE real-time updates - RED-GREEN-REFACTOR (TC-FE-036)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-5.2

#### StaffCallButton.jsx
- [ ] Staff call button - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-6.3

### 3.2 Admin Components

#### AdminLogin.jsx
- [ ] Admin login form - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-7.1

#### AdminDashboard.jsx
- [ ] Order list display - RED-GREEN-REFACTOR (TC-FE-037)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-8.1

- [ ] Status change - RED-GREEN-REFACTOR (TC-FE-038)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-8.2

- [ ] Order delete - RED-GREEN-REFACTOR (TC-FE-039)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-9.1

- [ ] SSE real-time orders - RED-GREEN-REFACTOR (TC-FE-040)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-8.1

#### OrderCard.jsx
- [ ] Order card display - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-8.1

#### MenuManagement.jsx
- [ ] Menu list display - RED-GREEN-REFACTOR (TC-FE-041)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-10.1

- [ ] Menu create - RED-GREEN-REFACTOR (TC-FE-042)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-10.2

- [ ] Menu update - RED-GREEN-REFACTOR (TC-FE-043)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-10.3

- [ ] Menu delete - RED-GREEN-REFACTOR (TC-FE-044)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-10.4

#### MenuForm.jsx
- [ ] Menu form - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-10.2, US-10.3

---

## Plan Step 4: Routing and Integration

### 4.1 App.js Routing
- [ ] Route configuration - RED-GREEN-REFACTOR
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass

### 4.2 Integration Tests
- [ ] Full order flow - RED-GREEN-REFACTOR (TC-FE-045)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-3.1, US-4.1, US-5.1

- [ ] Responsive layout - RED-GREEN-REFACTOR (TC-FE-046)
  - [ ] RED: Write failing test
  - [ ] GREEN: Minimal implementation
  - [ ] REFACTOR: Improve code quality
  - [ ] VERIFY: All tests pass
  - Story: US-6.1

---

## Plan Step 5: Additional Artifacts

### 5.1 Styling
- [ ] Create CSS modules for components
- [ ] Add responsive breakpoints
- [ ] Add loading states and animations

### 5.2 Documentation
- [ ] Update README.md with setup instructions
- [ ] Document component props and usage
- [ ] Create code summary in `aidlc-docs/construction/unit2-frontend/code/`

### 5.3 Configuration
- [ ] Configure Jest and React Testing Library
- [ ] Add test utilities and mocks
- [ ] Configure ESLint and Prettier

---

## Summary

**Total Steps**: 5 major steps
**Total Methods/Features**: ~60 TDD cycles
**Test Cases**: 46 test cases
**Stories Covered**: 24 user stories
**Estimated Completion**: All frontend functionality with comprehensive test coverage
