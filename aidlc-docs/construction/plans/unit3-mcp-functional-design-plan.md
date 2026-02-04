# Unit 3 (MCP Servers) - Functional Design Plan

## Unit Context
- **Unit Name**: MCP Servers
- **담당**: 개발자 3
- **디렉토리**: `/mcp` (core, customer, admin)
- **기술 스택**: Python, MCP SDK, httpx

## Assigned Stories
- US-11.1: 고객 Chatbot 테이블 컨텍스트 설정
- US-11.2: 고객 Chatbot 메뉴 조회 및 주문
- US-11.3: 고객 Chatbot 주문 조회 및 직원 호출
- US-12.1: 관리자 Chatbot 컨텍스트 설정
- US-12.2: 관리자 Chatbot 주문 관리
- US-12.3: 관리자 Chatbot 메뉴 관리

---

## Design Questions

### Question 1: MCP 세션 관리
MCP Tool 호출 간 컨텍스트(테이블 정보, 인증 토큰)를 어떻게 유지할까요?

A) MCP Server 메모리에 저장 (서버 재시작 시 초기화)
B) 파일 기반 저장 (~/.table-order-mcp/)
C) 매 Tool 호출 시 컨텍스트 파라미터로 전달
D) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: Redis 에서 세션관리 하는데, key 는 mcp의 session_id

---

### Question 2: 장바구니 관리 위치
고객용 MCP에서 장바구니를 어디서 관리할까요?

A) MCP Server 메모리 (세션 기반)
B) Backend API 호출 (서버 측 장바구니)
C) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: B

---

### Question 3: 에러 처리 방식
API 호출 실패 시 MCP Tool의 응답 형식은?

A) 에러 메시지 문자열 반환 (예: "주문 생성 실패: 세션이 만료되었습니다")
B) 구조화된 에러 객체 반환 (예: {"success": false, "error": "..."})
C) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: B

---

## Design Steps

### Step 1: 비즈니스 로직 모델
- [x] mcp-core 공유 모듈 설계
- [x] Customer MCP 비즈니스 로직
- [x] Admin MCP 비즈니스 로직

### Step 2: 도메인 엔티티
- [x] MCP 컨텍스트 모델 정의
- [x] Tool 입출력 모델 정의

### Step 3: 비즈니스 규칙
- [x] 컨텍스트 검증 규칙
- [x] Tool 호출 전제조건
- [x] 에러 처리 규칙

---

답변을 완료하셨으면 알려주세요.
