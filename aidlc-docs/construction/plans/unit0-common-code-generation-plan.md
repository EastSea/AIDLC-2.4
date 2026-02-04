# Unit 0 (Common) - Code Generation Plan

## Overview
공통 선행 작업: Infrastructure + OpenAPI + Mock API + env-setup.md

---

## Unit Context
- **Unit Name**: Common (Unit 0)
- **담당**: 3명 공동
- **목적**: 개발 환경 구축 및 API 계약 정의

---

## Generation Steps

### Step 1: 프로젝트 디렉토리 구조 생성
- [x] `/api` 디렉토리 구조 생성
- [x] `/web` 디렉토리 구조 생성
- [x] `/mcp` 디렉토리 구조 생성
- [x] `/infra` 디렉토리 생성
- [x] `/docs` 디렉토리 생성
- [x] `/mock` 디렉토리 생성

### Step 2: Infrastructure - Docker Compose
- [x] `/infra/docker-compose.yml` 생성 (PostgreSQL + Redis)

### Step 3: Environment Setup Guide
- [x] `/infra/env-setup.md` 생성 (환경 설정 가이드)

### Step 4: OpenAPI Specification
- [x] `/docs/openapi.yaml` 생성 (API 스펙 정의)

### Step 5: Mock API Server
- [x] `/mock/requirements.txt` 생성
- [x] `/mock/mock-server.py` 생성

### Step 6: Backend 기본 구조
- [x] `/api/requirements.txt` 생성
- [x] `/api/app/__init__.py` 생성
- [x] `/api/app/main.py` 생성 (FastAPI 앱 진입점)
- [x] `/api/app/config.py` 생성 (설정)
- [x] `/api/app/database.py` 생성 (DB 연결)

### Step 7: ~~Database Models & Migration~~ (Unit 1으로 이동)
- [x] Unit 1 (Backend)에서 구현 예정

### Step 8: Frontend 기본 구조
- [x] `/web/package.json` 생성
- [x] `/web/src/index.js` 생성
- [x] `/web/src/App.js` 생성

### Step 9: MCP 기본 구조
- [x] `/mcp/core/requirements.txt` 생성
- [x] `/mcp/core/__init__.py` 생성
- [x] `/mcp/customer/requirements.txt` 생성
- [x] `/mcp/admin/requirements.txt` 생성

---

## Completion Criteria
- `docker-compose up`으로 PostgreSQL + Redis 실행 가능
- Mock API Server 실행 가능
- 각 Unit 개발 시작 가능한 기본 구조 완성
