# Application Design Plan

## Overview
테이블오더 서비스의 컴포넌트 및 서비스 레이어 설계

---

## Part 1: Design Questions

아래 질문에 답변해 주세요.

---

### Question 1: 프론트엔드 프로젝트 구조
고객용 웹과 관리자용 웹을 어떻게 구성할까요?

A) 단일 React 프로젝트 (라우팅으로 분리)
B) 별도 React 프로젝트 2개 (customer-web, admin-web)
C) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: A

---

### Question 2: 백엔드 API 구조
FastAPI 백엔드의 API 구조를 어떻게 설계할까요?

A) 단일 FastAPI 앱 (라우터로 분리: /api/customer/*, /api/admin/*)
B) 별도 FastAPI 앱 2개 (customer-api, admin-api)
C) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: A

---

### Question 3: MCP Server 구조
고객용/관리자용 MCP Server를 어떻게 구성할까요?

A) 단일 MCP Server (Tools를 역할별로 분리)
B) 별도 MCP Server 2개 (customer-mcp, admin-mcp)
C) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: B

---

### Question 4: 데이터베이스 스키마 관리
DB 스키마 마이그레이션을 어떻게 관리할까요?

A) Alembic (SQLAlchemy 마이그레이션 도구)
B) 수동 SQL 스크립트
C) 기타 (아래 [Answer]: 태그 뒤에 설명해 주세요)

[Answer]: A

---

## Part 2: Design Steps

답변 완료 후 아래 단계에 따라 설계를 진행합니다.

### Step 1: 컴포넌트 정의
- [x] Backend API 컴포넌트 정의
- [x] Customer Frontend 컴포넌트 정의
- [x] Admin Frontend 컴포넌트 정의
- [x] MCP Server 컴포넌트 정의

### Step 2: 컴포넌트 메서드 정의
- [x] API 엔드포인트 정의
- [x] Frontend 주요 기능 정의
- [x] MCP Tools 정의

### Step 3: 서비스 레이어 설계
- [x] 비즈니스 서비스 정의
- [x] 서비스 간 상호작용 정의

### Step 4: 컴포넌트 의존성 정의
- [x] 컴포넌트 간 의존성 매트릭스
- [x] 데이터 흐름 정의

### Step 5: Entity-Model-Table 매핑 (추가)
- [x] Frontend Entity 정의
- [x] Backend Model (Pydantic + SQLAlchemy) 정의
- [x] Database Table 설계

### Step 6: Message Flow 설계 (추가)
- [x] 주요 비즈니스 플로우별 메시지 흐름 정의

---

답변을 완료하셨으면 알려주세요.
