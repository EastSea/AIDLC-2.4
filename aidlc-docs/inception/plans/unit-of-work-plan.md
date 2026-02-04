# Unit of Work Plan

## Overview
테이블오더 서비스의 작업 단위(Unit of Work) 분해 계획
**팀 구성**: 3명 동시 개발

---

## Part 1: Planning Questions

아래 질문에 답변해 주세요.

---

### Question 1: 3명 역할 분배
3명의 개발자에게 어떻게 역할을 분배할까요?

A) 레이어별 분배
```
개발자 1: Backend API (FastAPI, DB, SSE)
개발자 2: Frontend (React - 고객용 + 관리자용)
개발자 3: MCP Servers (mcp-core + customer-mcp + admin-mcp)
```

B) 기능별 분배
```
개발자 1: 고객용 전체 (Customer Frontend + Customer API + Customer MCP)
개발자 2: 관리자용 전체 (Admin Frontend + Admin API + Admin MCP)
개발자 3: 공통/인프라 (DB, Auth, SSE, mcp-core, Docker)
```

C) 하이브리드 분배
```
개발자 1: Backend API + Infrastructure (FastAPI, DB, Docker)
개발자 2: Frontend 전체 (React - 고객용 + 관리자용)
개발자 3: MCP Servers 전체 (mcp-core + customer-mcp + admin-mcp)
```

D) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: A

---

### Question 2: 통합 시점
각 개발자의 작업을 언제 통합할까요?

A) 매일 통합 (CI/CD 기반)
B) 주요 기능 완료 시 통합
C) 각 Phase 완료 시 통합
D) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: C

---

### Question 3: API 계약 관리
Frontend와 Backend 간 API 계약을 어떻게 관리할까요?

A) OpenAPI (Swagger) 스펙 먼저 정의 → 각자 개발
B) Backend가 API 먼저 개발 → Frontend가 따라감
C) Mock Server 활용 (Frontend가 Mock으로 먼저 개발)
D) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: A

---

### Question 4: 프로젝트 디렉토리 구조
프로젝트 루트의 디렉토리 구조를 어떻게 구성할까요?

A) 모노레포 (단일 저장소에 모든 프로젝트)
```
/backend
/frontend
/mcp-core
/customer-mcp
/admin-mcp
/docker
```

B) 기능별 분리
```
/api (backend)
/web (frontend)
/mcp/core
/mcp/customer
/mcp/admin
/infra (docker)
```

C) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: B

---

## Part 2: Generation Steps

답변 완료 후 아래 단계에 따라 Unit을 생성합니다.

### Step 1: Unit 정의 (3명 기준)
- [x] 개발자 1 담당 Unit 정의
- [x] 개발자 2 담당 Unit 정의
- [x] 개발자 3 담당 Unit 정의

### Step 2: Unit 의존성 정의
- [x] Unit 간 의존성 매트릭스 작성
- [x] 병렬 개발 가능 영역 식별
- [x] 통합 포인트 정의

### Step 3: Story-Unit 매핑
- [x] 각 User Story를 담당 개발자/Unit에 매핑

### Step 4: 검증
- [x] 모든 Story가 Unit에 할당되었는지 확인
- [x] 3명 간 작업량 균형 확인
- [x] 의존성으로 인한 블로킹 최소화 확인

---

답변을 완료하셨으면 알려주세요.
