# Swagger UI 테스트 데이터

## 접속 URL
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 1. Customer Auth (고객 인증)

### POST `/api/customer/auth/login` - 테이블 로그인
```json
{
  "store_code": "TEST001",
  "table_number": 1,
  "password": "1234"
}
```

**응답 예시:**
```json
{
  "token": "eyJhbGc...",
  "table_id": "9144f6b1-a2a1-4616-9515-02520526ff6e",
  "session_id": "e2733843-31fb-457a-a9ba-bc8704e6f312",
  "table_number": 1
}
```

> 💡 **session_id**를 복사해서 Cart API에 사용하세요!

---

## 2. Customer Cart (장바구니)

### GET `/api/customer/cart` - 장바구니 조회
**Query Parameters:**
- `session_id`: `e2733843-31fb-457a-a9ba-bc8704e6f312` (로그인 응답에서 받은 값)

---

### POST `/api/customer/cart` - 장바구니 추가

**예시 1: 기본 메뉴 추가**
```json
{
  "session_id": "e2733843-31fb-457a-a9ba-bc8704e6f312",
  "menu_id": "menu-5",
  "quantity": 2
}
```

**예시 2: 옵션이 있는 메뉴 추가**
```json
{
  "session_id": "e2733843-31fb-457a-a9ba-bc8704e6f312",
  "menu_id": "menu-4",
  "quantity": 1,
  "options": "미디움 레어"
}
```

**예시 3: 세트 메뉴 추가**
```json
{
  "session_id": "e2733843-31fb-457a-a9ba-bc8704e6f312",
  "menu_id": "menu-1",
  "quantity": 1,
  "options": "소스 추가"
}
```

---

### PATCH `/api/customer/cart/{item_id}` - 수량 변경
**Path Parameter:**
- `item_id`: `f0bd2573-5f71-416d-a280-82b2cd194a19` (장바구니 조회 응답에서 받은 item의 id)

**Request Body:**
```json
{
  "quantity": 3
}
```

---

### DELETE `/api/customer/cart/{item_id}` - 항목 삭제
**Path Parameter:**
- `item_id`: `f0bd2573-5f71-416d-a280-82b2cd194a19`

---

### DELETE `/api/customer/cart` - 장바구니 비우기
**Query Parameters:**
- `session_id`: `e2733843-31fb-457a-a9ba-bc8704e6f312`

---

## 3. 사용 가능한 메뉴 ID

| Menu ID | 메뉴명 | 가격 | 카테고리 |
|---------|--------|------|----------|
| `menu-1` | BBQ파티팩 2~3인 세트 | 68,000원 | 세트메뉴 |
| `menu-2` | 안심 스테이크 2인 세트 | 54,000원 | 세트메뉴 |
| `menu-3` | 바비큐 폭립 파티 3~4인 세트 | 69,000원 | 세트메뉴 |
| `menu-4` | 티본 스테이크 | 45,000원 | 스테이크 |
| `menu-5` | 까르보나라 | 18,000원 | 파스타 |

---

## 4. 테스트 시나리오

### 시나리오 1: 기본 장바구니 플로우
1. **로그인** → `session_id` 획득
2. **장바구니 조회** → 빈 장바구니 확인
3. **메뉴 추가** → 까르보나라 2개 추가
4. **메뉴 추가** → 티본 스테이크 1개 추가
5. **장바구니 조회** → 총 2개 항목, 81,000원 확인
6. **수량 변경** → 까르보나라 2개 → 3개
7. **항목 삭제** → 티본 스테이크 삭제
8. **장바구니 비우기** → 전체 삭제

### 시나리오 2: 옵션 테스트
1. **로그인** → `session_id` 획득
2. **메뉴 추가** → 까르보나라 2개 (옵션 없음)
3. **메뉴 추가** → 까르보나라 1개 (옵션: "매운맛")
4. **장바구니 조회** → 2개 항목으로 분리되어 있는지 확인

### 시나리오 3: 중복 추가 테스트
1. **로그인** → `session_id` 획득
2. **메뉴 추가** → 까르보나라 2개
3. **메뉴 추가** → 까르보나라 1개 (동일 메뉴)
4. **장바구니 조회** → 수량이 3개로 증가했는지 확인

---

## 5. 에러 케이스 테스트

### 존재하지 않는 메뉴
```json
{
  "session_id": "e2733843-31fb-457a-a9ba-bc8704e6f312",
  "menu_id": "invalid-menu-id",
  "quantity": 1
}
```
**예상 응답:** `{"detail": "Menu not found"}`

### 존재하지 않는 항목 수정
- Path: `/api/customer/cart/invalid-item-id`
- **예상 응답:** `{"detail": "Cart item not found"}`

---

## 6. 다른 테이블로 테스트

테이블 2번으로 로그인:
```json
{
  "store_code": "TEST001",
  "table_number": 2,
  "password": "1234"
}
```

테이블 3번으로 로그인:
```json
{
  "store_code": "TEST001",
  "table_number": 3,
  "password": "1234"
}
```

> 각 테이블은 독립적인 `session_id`를 가지며, 장바구니도 분리됩니다.
