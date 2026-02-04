# Requirements Verification Questions

요구사항 분석을 완료하기 위해 아래 질문에 답변해 주세요.
각 질문의 [Answer]: 태그 뒤에 선택한 옵션의 알파벳을 입력해 주세요.

---

## Question 1
프론트엔드 기술 스택으로 어떤 것을 선호하시나요?

A) React (가장 널리 사용, 풍부한 생태계)
B) Vue.js (학습 곡선 낮음, 직관적)
C) Next.js (React 기반, SSR 지원)
D) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: A

---

## Question 2
백엔드 기술 스택으로 어떤 것을 선호하시나요?

A) Node.js + Express (JavaScript 풀스택, 빠른 개발)
B) Node.js + NestJS (TypeScript, 구조화된 아키텍처)
C) Python + FastAPI (빠른 성능, 자동 문서화)
D) Java + Spring Boot (엔터프라이즈급, 안정성)
E) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: C

---

## Question 3
데이터베이스로 어떤 것을 사용하시겠습니까?

A) PostgreSQL (관계형, 강력한 기능)
B) MySQL (관계형, 널리 사용)
C) MongoDB (NoSQL, 유연한 스키마)
D) DynamoDB (AWS 관리형 NoSQL)
E) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: A

---

## Question 4
배포 환경은 어떻게 계획하고 계신가요?

A) AWS (EC2, ECS, Lambda 등)
B) 로컬/온프레미스 서버
C) Docker 컨테이너 (배포 환경 미정)
D) 기타 클라우드 (Azure, GCP 등)
E) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: 로컬 환경은 로컬서버로 구성하되 DEV/STG/PRD는 docker image로 배포할거야.

---

## Question 5
MVP 개발 우선순위에서 가장 먼저 완성하고 싶은 기능은 무엇인가요?

A) 고객용 기능 우선 (메뉴 조회, 장바구니, 주문)
B) 관리자용 기능 우선 (주문 모니터링, 테이블 관리)
C) 전체 기능 동시 개발
D) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: A

---

## Question 6
실시간 주문 모니터링의 SSE(Server-Sent Events) 구현 범위는 어떻게 하시겠습니까?

A) 기본 구현 (새 주문 알림만)
B) 전체 구현 (주문 상태 변경, 테이블 상태 모두 실시간)
C) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: B

---

## Question 7
메뉴 이미지는 어떻게 관리하시겠습니까? (이미지 리사이징/최적화는 제외 범위)

A) 외부 URL 직접 입력 (이미지 호스팅 서비스 사용)
B) 서버에 정적 파일로 저장 (단순 업로드만)
C) S3 등 클라우드 스토리지 사용
D) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: 서버에 업로드 API를 구현하고, Postgrs DB에 이미지 파일을 저장하도록 해줘.

---

답변을 완료하셨으면 알려주세요.
