# Test Plan for Unit 2 (Frontend)

## Unit Overview
- **Unit**: unit2-frontend
- **Stories**: 24 stories (US-1.2, US-2.1~2.3, US-3.1~3.3, US-4.1~4.2, US-5.1~5.2, US-6.1~6.3, US-7.1, US-8.1~8.3, US-9.1~9.3, US-10.1~10.5)
- **Technology**: React 18, React Router 6, Axios, Jest, React Testing Library

---

## API Service Layer Tests

### authService.js

#### TC-FE-001: loginTable - 성공 케이스
- **Given**: Valid store code, table number, password
- **When**: loginTable() is called
- **Then**: Returns auth response with token, tableId, sessionId
- **Story**: US-1.2
- **Status**: ⬜ Not Started

#### TC-FE-002: loginTable - 실패 케이스
- **Given**: Invalid credentials
- **When**: loginTable() is called
- **Then**: Throws API error
- **Story**: US-1.2
- **Status**: ⬜ Not Started

#### TC-FE-003: loginAdmin - 성공 케이스
- **Given**: Valid admin credentials
- **When**: loginAdmin() is called
- **Then**: Returns admin auth response
- **Story**: US-7.1
- **Status**: ⬜ Not Started

### menuService.js

#### TC-FE-004: getCategories - 카테고리 목록 조회
- **Given**: API returns category list
- **When**: getCategories() is called
- **Then**: Returns array of categories
- **Story**: US-2.1
- **Status**: ⬜ Not Started

#### TC-FE-005: getMenus - 전체 메뉴 조회
- **Given**: No filters provided
- **When**: getMenus() is called
- **Then**: Returns all menus
- **Story**: US-2.1
- **Status**: ⬜ Not Started

#### TC-FE-006: getMenus - 카테고리 필터
- **Given**: categoryId provided
- **When**: getMenus(categoryId) is called
- **Then**: Returns filtered menus
- **Story**: US-2.1
- **Status**: ⬜ Not Started

#### TC-FE-007: getMenus - 인원수 필터
- **Given**: servingSize provided
- **When**: getMenus(null, servingSize) is called
- **Then**: Returns filtered menus by serving size
- **Story**: US-2.3
- **Status**: ⬜ Not Started

#### TC-FE-008: getMenuDetail - 메뉴 상세 조회
- **Given**: Valid menuId
- **When**: getMenuDetail(menuId) is called
- **Then**: Returns menu details
- **Story**: US-2.2
- **Status**: ⬜ Not Started

### orderService.js

#### TC-FE-009: createOrder - 주문 생성 성공
- **Given**: Valid sessionId and items
- **When**: createOrder() is called
- **Then**: Returns orderId and orderNumber
- **Story**: US-4.1
- **Status**: ⬜ Not Started

#### TC-FE-010: createOrder - 주문 생성 실패
- **Given**: Invalid data
- **When**: createOrder() is called
- **Then**: Throws API error
- **Story**: US-4.2
- **Status**: ⬜ Not Started

#### TC-FE-011: getOrders - 주문 내역 조회
- **Given**: Valid sessionId
- **When**: getOrders(sessionId) is called
- **Then**: Returns order array
- **Story**: US-5.1
- **Status**: ⬜ Not Started

### staffService.js

#### TC-FE-012: callStaff - 직원 호출
- **Given**: Valid tableId
- **When**: callStaff(tableId) is called
- **Then**: Returns success response
- **Story**: US-6.3
- **Status**: ⬜ Not Started

---

## Custom Hooks Tests

### useCart.js

#### TC-FE-013: addItem - 장바구니에 아이템 추가
- **Given**: Empty cart
- **When**: addItem() is called with menu
- **Then**: Cart contains the item
- **Story**: US-3.1
- **Status**: ⬜ Not Started

#### TC-FE-014: addItem - 동일 아이템 추가 시 수량 증가
- **Given**: Cart has item with quantity 1
- **When**: addItem() is called with same menu
- **Then**: Item quantity becomes 2
- **Story**: US-3.1
- **Status**: ⬜ Not Started

#### TC-FE-015: updateQuantity - 수량 증가
- **Given**: Cart has item with quantity 1
- **When**: updateQuantity(menuId, 2) is called
- **Then**: Item quantity becomes 2
- **Story**: US-3.2
- **Status**: ⬜ Not Started

#### TC-FE-016: updateQuantity - 수량 0으로 설정 시 삭제
- **Given**: Cart has item
- **When**: updateQuantity(menuId, 0) is called
- **Then**: Item is removed from cart
- **Story**: US-3.2
- **Status**: ⬜ Not Started

#### TC-FE-017: removeItem - 아이템 삭제
- **Given**: Cart has item
- **When**: removeItem(menuId) is called
- **Then**: Item is removed from cart
- **Story**: US-3.2
- **Status**: ⬜ Not Started

#### TC-FE-018: clearCart - 장바구니 비우기
- **Given**: Cart has multiple items
- **When**: clearCart() is called
- **Then**: Cart is empty
- **Story**: US-4.1
- **Status**: ⬜ Not Started

#### TC-FE-019: totalAmount - 총 금액 계산
- **Given**: Cart has items with different prices and quantities
- **When**: totalAmount is accessed
- **Then**: Returns correct total
- **Story**: US-3.1
- **Status**: ⬜ Not Started

#### TC-FE-020: localStorage persistence - 장바구니 유지
- **Given**: Cart has items
- **When**: Page is refreshed
- **Then**: Cart items are restored from localStorage
- **Story**: US-3.3
- **Status**: ⬜ Not Started

### useAuth.js

#### TC-FE-021: login - 로그인 성공
- **Given**: Valid credentials
- **When**: login() is called
- **Then**: isAuthenticated becomes true, user is set
- **Story**: US-1.2, US-7.1
- **Status**: ⬜ Not Started

#### TC-FE-022: logout - 로그아웃
- **Given**: User is authenticated
- **When**: logout() is called
- **Then**: isAuthenticated becomes false, user is null
- **Story**: US-7.1
- **Status**: ⬜ Not Started

### useIdleTimeout.js

#### TC-FE-023: Idle timeout - 타임아웃 발생
- **Given**: No user activity for timeout duration
- **When**: Timeout expires
- **Then**: onTimeout callback is called
- **Story**: US-6.2
- **Status**: ⬜ Not Started

#### TC-FE-024: Idle timeout - 활동 시 리셋
- **Given**: User is idle
- **When**: User interacts with page
- **Then**: Timeout is reset
- **Story**: US-6.2
- **Status**: ⬜ Not Started

---

## Component Tests

### MenuBrowser.jsx

#### TC-FE-025: 카테고리 목록 렌더링
- **Given**: Categories are loaded
- **When**: Component renders
- **Then**: All categories are displayed
- **Story**: US-2.1
- **Status**: ⬜ Not Started

#### TC-FE-026: 카테고리 선택 시 메뉴 필터링
- **Given**: Component is rendered
- **When**: User clicks a category
- **Then**: Only menus from that category are shown
- **Story**: US-2.1
- **Status**: ⬜ Not Started

#### TC-FE-027: 인원수 필터 적용
- **Given**: Component is rendered
- **When**: User selects serving size filter
- **Then**: Menus are filtered by serving size
- **Story**: US-2.3
- **Status**: ⬜ Not Started

### MenuCard.jsx

#### TC-FE-028: 메뉴 정보 표시
- **Given**: Menu data is provided
- **When**: Component renders
- **Then**: Menu name, price, image are displayed
- **Story**: US-2.1
- **Status**: ⬜ Not Started

#### TC-FE-029: 장바구니 담기 버튼
- **Given**: Component is rendered
- **When**: User clicks add to cart button
- **Then**: onAddToCart callback is called with menu
- **Story**: US-3.1
- **Status**: ⬜ Not Started

### Cart.jsx

#### TC-FE-030: 장바구니 아이템 표시
- **Given**: Cart has items
- **When**: Component renders
- **Then**: All cart items are displayed with quantity and price
- **Story**: US-3.1
- **Status**: ⬜ Not Started

#### TC-FE-031: 수량 증가/감소 버튼
- **Given**: Cart has item
- **When**: User clicks +/- buttons
- **Then**: Item quantity is updated
- **Story**: US-3.2
- **Status**: ⬜ Not Started

#### TC-FE-032: 총 금액 표시
- **Given**: Cart has items
- **When**: Component renders
- **Then**: Total amount is displayed correctly
- **Story**: US-3.1
- **Status**: ⬜ Not Started

#### TC-FE-033: 주문하기 버튼
- **Given**: Cart has items
- **When**: User clicks checkout button
- **Then**: Order is created and cart is cleared
- **Story**: US-4.1
- **Status**: ⬜ Not Started

### OrderHistory.jsx

#### TC-FE-034: 주문 내역 표시
- **Given**: User has order history
- **When**: Component renders
- **Then**: All orders are displayed with details
- **Story**: US-5.1
- **Status**: ⬜ Not Started

#### TC-FE-035: 주문 상태 표시
- **Given**: Orders have different statuses
- **When**: Component renders
- **Then**: Each order shows correct status badge
- **Story**: US-5.2
- **Status**: ⬜ Not Started

#### TC-FE-036: SSE 실시간 업데이트
- **Given**: Component is mounted
- **When**: Order status changes on server
- **Then**: UI updates automatically
- **Story**: US-5.2
- **Status**: ⬜ Not Started

### AdminDashboard.jsx

#### TC-FE-037: 주문 목록 표시
- **Given**: Admin is logged in
- **When**: Component renders
- **Then**: All pending orders are displayed
- **Story**: US-8.1
- **Status**: ⬜ Not Started

#### TC-FE-038: 주문 상태 변경
- **Given**: Order is displayed
- **When**: Admin changes order status
- **Then**: Status is updated on server and UI
- **Story**: US-8.2
- **Status**: ⬜ Not Started

#### TC-FE-039: 주문 삭제
- **Given**: Order is displayed
- **When**: Admin clicks delete button
- **Then**: Order is removed from list
- **Story**: US-9.1
- **Status**: ⬜ Not Started

#### TC-FE-040: SSE 실시간 주문 수신
- **Given**: Dashboard is open
- **When**: New order is created
- **Then**: Order appears in dashboard automatically
- **Story**: US-8.1
- **Status**: ⬜ Not Started

### MenuManagement.jsx

#### TC-FE-041: 메뉴 목록 표시
- **Given**: Admin is logged in
- **When**: Component renders
- **Then**: All menus are displayed
- **Story**: US-10.1
- **Status**: ⬜ Not Started

#### TC-FE-042: 메뉴 생성
- **Given**: Admin clicks create button
- **When**: Form is submitted with valid data
- **Then**: New menu is created and added to list
- **Story**: US-10.2
- **Status**: ⬜ Not Started

#### TC-FE-043: 메뉴 수정
- **Given**: Admin clicks edit button
- **When**: Form is submitted with updated data
- **Then**: Menu is updated in list
- **Story**: US-10.3
- **Status**: ⬜ Not Started

#### TC-FE-044: 메뉴 삭제
- **Given**: Admin clicks delete button
- **When**: Deletion is confirmed
- **Then**: Menu is removed from list
- **Story**: US-10.4
- **Status**: ⬜ Not Started

---

## Integration Tests

#### TC-FE-045: 전체 주문 플로우
- **Given**: Customer is on menu page
- **When**: Customer adds items, goes to cart, and checks out
- **Then**: Order is created and appears in order history
- **Story**: US-3.1, US-4.1, US-5.1
- **Status**: ⬜ Not Started

#### TC-FE-046: 반응형 레이아웃
- **Given**: App is loaded
- **When**: Viewport size changes (mobile, tablet, desktop)
- **Then**: Layout adapts correctly
- **Story**: US-6.1
- **Status**: ⬜ Not Started

---

## Requirements Coverage

| Requirement ID | Test Cases | Status |
|---------------|------------|--------|
| US-1.2 | TC-FE-001, TC-FE-002, TC-FE-021 | ⬜ Pending |
| US-2.1 | TC-FE-004, TC-FE-005, TC-FE-006, TC-FE-025, TC-FE-026, TC-FE-028 | ⬜ Pending |
| US-2.2 | TC-FE-008 | ⬜ Pending |
| US-2.3 | TC-FE-007, TC-FE-027 | ⬜ Pending |
| US-3.1 | TC-FE-013, TC-FE-014, TC-FE-019, TC-FE-029, TC-FE-030, TC-FE-045 | ⬜ Pending |
| US-3.2 | TC-FE-015, TC-FE-016, TC-FE-017, TC-FE-031 | ⬜ Pending |
| US-3.3 | TC-FE-020 | ⬜ Pending |
| US-4.1 | TC-FE-009, TC-FE-018, TC-FE-033, TC-FE-045 | ⬜ Pending |
| US-4.2 | TC-FE-010 | ⬜ Pending |
| US-5.1 | TC-FE-011, TC-FE-034, TC-FE-045 | ⬜ Pending |
| US-5.2 | TC-FE-035, TC-FE-036 | ⬜ Pending |
| US-6.1 | TC-FE-046 | ⬜ Pending |
| US-6.2 | TC-FE-023, TC-FE-024 | ⬜ Pending |
| US-6.3 | TC-FE-012 | ⬜ Pending |
| US-7.1 | TC-FE-003, TC-FE-021, TC-FE-022 | ⬜ Pending |
| US-8.1 | TC-FE-037, TC-FE-040 | ⬜ Pending |
| US-8.2 | TC-FE-038 | ⬜ Pending |
| US-9.1 | TC-FE-039 | ⬜ Pending |
| US-10.1 | TC-FE-041 | ⬜ Pending |
| US-10.2 | TC-FE-042 | ⬜ Pending |
| US-10.3 | TC-FE-043 | ⬜ Pending |
| US-10.4 | TC-FE-044 | ⬜ Pending |

**Total Test Cases**: 46
**Coverage**: All 24 user stories covered
