# Table-Order Service Requirements

## Intent Analysis Summary

| 항목 | 내용 |
|------|------|
| **User Request** | 테이블오더 서비스 개발 (MVP) |
| **Request Type** | New Project (Greenfield) |
| **Scope Estimate** | System-wide (프론트엔드 + 백엔드 + 데이터베이스) |
| **Complexity Estimate** | Moderate (다중 컴포넌트, SSE 실시간 통신 포함) |

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React (반응형 웹, White Theme) |
| **Backend** | Python + FastAPI |
| **Database** | PostgreSQL |
| **Real-time** | Server-Sent Events (SSE) |
| **MCP Server** | Python (고객용 + 관리자용) |
| **Local Dev** | Docker Compose (PostgreSQL) |
| **Deployment** | 로컬: 로컬 서버 / DEV·STG·PRD: Docker Image |

---

## Functional Requirements

### FR-1: 고객용 기능 (Customer Features)

#### FR-1.1: 테이블 태블릿 자동 로그인
- 초기 설정: 매장 식별자, 테이블 번호, 테이블 비밀번호 입력
- 로그인 정보 로컬 저장 후 자동 로그인

#### FR-1.2: 메뉴 조회 및 탐색
- 메뉴 화면이 기본 화면
- 카테고리별 메뉴 분류 및 표시
- 메뉴 상세: 메뉴명, 가격, 설명, 이미지
- 터치 친화적 UI (최소 44x44px 버튼)

#### FR-1.3: 장바구니 관리
- 메뉴 추가/삭제, 수량 조절
- 총 금액 실시간 계산
- 로컬 저장 (페이지 새로고침 시 유지)

#### FR-1.4: 주문 생성
- 주문 내역 최종 확인 및 확정
- 주문 성공: 주문 번호 표시 → 장바구니 비우기 → 메뉴 화면 리다이렉트
- 주문 실패: 에러 메시지 표시, 장바구니 유지

#### FR-1.5: 주문 내역 조회
- 현재 테이블 세션 주문만 표시
- 주문 시간 순 정렬
- 주문 상태: 대기중/준비중/완료

#### FR-1.6: 반응형 웹 UI
- Mobile (~480px), Tablet (481px~1024px), Kiosk (1025px~) breakpoints
- 밝은 White Theme 적용
- **레이아웃 구성** (EOS POS 스타일 참고):
  - 좌측: 카테고리 메뉴 (세로 배치)
  - 중앙: 메뉴 그리드 (이미지 + 메뉴명 + 가격)
  - 우측 상단: 테이블 번호 표시
  - 상단: Idle 타이머 카운트다운 표시
  - 하단: 장바구니, 주문내역, 직원호출 버튼
  - 인원수 필터 (전체, 1~2인, 3~4인 등)

#### FR-1.7: Idle Timeout (자동 홈 복귀)
- 60초간 입력 없으면 자동으로 Home(메뉴) 화면으로 복귀
- 입력/이벤트 발생 시 60초 타이머 초기화

### FR-2: 관리자용 기능 (Admin Features)

#### FR-2.1: 매장 인증
- 매장 식별자, 사용자명, 비밀번호 입력
- JWT 토큰 기반 인증, 16시간 세션 유지
- 비밀번호 bcrypt 해싱

#### FR-2.2: 실시간 주문 모니터링
- SSE 기반 실시간 업데이트 (2초 이내)
- 그리드/대시보드 레이아웃 (테이블별 카드)
- 주문 상태 변경 (대기중/준비중/완료)
- 신규 주문 시각적 강조

#### FR-2.3: 테이블 관리
- 테이블 초기 설정 (번호, 비밀번호)
- 주문 삭제 (직권 수정)
- 테이블 세션 종료 (이용 완료 처리)
- 과거 주문 내역 조회

#### FR-2.4: 메뉴 관리
- 메뉴 CRUD (등록, 조회, 수정, 삭제)
- 메뉴 정보: 메뉴명, 가격, 설명, 카테고리, 이미지
- 메뉴 노출 순서 조정

### FR-3: MCP Server (Chatbot Integration)

#### FR-3.1: MCP 공유 서비스 모듈 (mcp-core)
- Customer MCP와 Admin MCP가 공유하는 서비스 모듈
- Backend API 클라이언트 및 공통 로직 포함
- 재사용성과 리팩토링 용이성 확보

#### FR-3.2: 고객용 MCP Server
- Agent Chatbot(MCP Client)과 연동
- **필수 사전 체크**: 모든 Tool 호출 전 테이블 컨텍스트 설정 필수
  - `set_table_context` Tool로 테이블 식별 (store_code, table_number, password)
  - 컨텍스트 미설정 시 다른 Tool 호출 불가
- 고객용 웹사이트 기능을 MCP Tool로 제공:
  - 테이블 정보 조회
  - 메뉴 조회 (카테고리별, 인원수별 필터)
  - 장바구니 관리 (추가, 수량 조절, 삭제)
  - 주문 생성
  - 주문 내역 조회
  - 직원 호출

#### FR-3.3: 관리자용 MCP Server
- Agent Chatbot(MCP Client)과 연동
- **필수 사전 체크**: 모든 Tool 호출 전 관리자 컨텍스트 설정 필수
  - `set_admin_context` Tool로 관리자 인증 (store_code, username, password)
- 관리자용 웹사이트 기능을 MCP Tool로 제공:
  - 실시간 주문 현황 조회
  - 주문 상태 변경
  - 주문 삭제
  - 테이블 이용 완료 처리
  - 과거 주문 내역 조회
  - 메뉴 관리 (CRUD)

---

## Non-Functional Requirements

| ID | 항목 | 요구사항 |
|----|------|----------|
| NFR-1 | 성능 | SSE 주문 알림 2초 이내, 페이지 로딩 3초 이내 |
| NFR-2 | 보안 | JWT 인증, bcrypt 해싱, 로그인 시도 제한 |
| NFR-3 | 사용성 | 터치 친화적 UI (최소 44x44px), 반응형, White Theme |
| NFR-4 | 배포 | 로컬: 로컬 서버 / DEV·STG·PRD: Docker Image |

---

## Infrastructure Requirements

### 로컬 개발 환경
- PostgreSQL Docker Compose 구성
- 로컬 서버 실행 환경

---

## Data Requirements

### 이미지 저장
- 메뉴 이미지 업로드 API 구현
- PostgreSQL DB에 이미지 파일 저장

---

## Constraints (제외 범위)

- 결제 관련 (PG사 연동, 영수증, 환불, 포인트/쿠폰)
- 복잡한 인증 (OAuth, SNS 로그인, 2FA)
- 이미지 리사이징/최적화
- 알림 시스템 (푸시, SMS, 이메일)
- 주방 기능, 예약, 리뷰, 다국어
- 외부 연동 (배달, POS, 소셜, 지도)

---

## Development Priority

1. **Phase 1**: 고객용 기능 (메뉴 조회, 장바구니, 주문)
2. **Phase 2**: 관리자용 기능 (주문 모니터링, 테이블 관리, 메뉴 관리)
3. **Phase 3**: MCP Server (고객용 MCP Server, 관리자용 MCP Server)
