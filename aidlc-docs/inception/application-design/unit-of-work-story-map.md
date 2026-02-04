# Unit of Work - Story Mapping

## Story to Unit Mapping

### Unit 0: Common (공통 선행)
| Story ID | Story Name | 비고 |
|----------|------------|------|
| - | Infrastructure Setup | Docker Compose, PostgreSQL, Redis |
| - | OpenAPI Spec Definition | API 계약 정의 |
| - | Mock API Server | Frontend/MCP 개발 지원 |
| - | Environment Setup Guide | env-setup.md |

---

### Unit 1: Backend API (개발자 1)

#### 고객용 API
| Story ID | Story Name |
|----------|------------|
| US-1.1 | 테이블 초기 설정 |
| US-1.2 | 자동 로그인 |
| US-2.1 | 카테고리별 메뉴 조회 |
| US-2.2 | 메뉴 상세 정보 확인 |
| US-2.3 | 인원수별 메뉴 필터 |
| US-4.1 | 주문 확정 |
| US-4.2 | 주문 실패 처리 |
| US-5.1 | 현재 세션 주문 조회 |
| US-5.2 | 주문 상태 확인 |
| US-6.3 | 직원 호출 |

#### 관리자용 API
| Story ID | Story Name |
|----------|------------|
| US-7.1 | 관리자 로그인 |
| US-7.2 | 자동 로그아웃 |
| US-8.1 | 실시간 주문 대시보드 (SSE) |
| US-8.2 | 주문 상태 변경 |
| US-8.3 | 주문 상세 보기 |
| US-9.1 | 주문 삭제 |
| US-9.2 | 테이블 이용 완료 |
| US-9.3 | 과거 주문 내역 조회 |
| US-10.1 | 메뉴 조회 |
| US-10.2 | 메뉴 등록 |
| US-10.3 | 메뉴 수정 |
| US-10.4 | 메뉴 삭제 |
| US-10.5 | 메뉴 순서 조정 |

---

### Unit 2: Frontend (개발자 2)

#### 고객용 UI
| Story ID | Story Name |
|----------|------------|
| US-1.2 | 자동 로그인 (UI) |
| US-2.1 | 카테고리별 메뉴 조회 (UI) |
| US-2.2 | 메뉴 상세 정보 확인 (UI) |
| US-2.3 | 인원수별 메뉴 필터 (UI) |
| US-3.1 | 메뉴 장바구니 담기 |
| US-3.2 | 장바구니 수량 조절 |
| US-3.3 | 장바구니 유지 |
| US-4.1 | 주문 확정 (UI) |
| US-4.2 | 주문 실패 처리 (UI) |
| US-5.1 | 현재 세션 주문 조회 (UI) |
| US-5.2 | 주문 상태 확인 (UI) |
| US-6.1 | 반응형 레이아웃 |
| US-6.2 | Idle Timeout |
| US-6.3 | 직원 호출 (UI) |

#### 관리자용 UI
| Story ID | Story Name |
|----------|------------|
| US-7.1 | 관리자 로그인 (UI) |
| US-8.1 | 실시간 주문 대시보드 (UI) |
| US-8.2 | 주문 상태 변경 (UI) |
| US-8.3 | 주문 상세 보기 (UI) |
| US-9.1 | 주문 삭제 (UI) |
| US-9.2 | 테이블 이용 완료 (UI) |
| US-9.3 | 과거 주문 내역 조회 (UI) |
| US-10.1~5 | 메뉴 관리 (UI) |

---

### Unit 3: MCP Servers (개발자 3)

#### 고객용 MCP
| Story ID | Story Name |
|----------|------------|
| US-11.1 | 테이블 컨텍스트 설정 |
| US-11.2 | 메뉴 조회 및 주문 |
| US-11.3 | 주문 조회 및 직원 호출 |

#### 관리자용 MCP
| Story ID | Story Name |
|----------|------------|
| US-12.1 | 관리자 컨텍스트 설정 |
| US-12.2 | 주문 관리 |
| US-12.3 | 메뉴 관리 |

---

## Summary

| Unit | Story Count | 담당자 |
|------|-------------|--------|
| Unit 0 (Common) | 4 tasks | 3명 공동 |
| Unit 1 (Backend) | 23 stories | 개발자 1 |
| Unit 2 (Frontend) | 24 stories | 개발자 2 |
| Unit 3 (MCP) | 6 stories | 개발자 3 |

**Note**: 일부 Story는 Backend + Frontend 양쪽에서 구현 필요 (API + UI)
