# Unit 3 (MCP Servers) - NFR Requirements Plan

## Unit Context
- **Unit Name**: MCP Servers
- **디렉토리**: `/mcp` (core, customer, admin)
- **기술 스택**: Python, MCP SDK, httpx, Redis

---

## NFR Questions

### Question 1: 응답 시간 요구사항
MCP Tool 호출의 최대 허용 응답 시간은?

A) 1초 이내
B) 3초 이내
C) 5초 이내
D) 제한 없음 (Backend 응답에 의존)

[Answer]: A

---

### Question 2: 동시 세션 수
MCP Server당 동시 처리 가능한 세션 수는?

A) 10개 이하 (개발/테스트용)
B) 50개 (소규모 매장)
C) 100개 이상 (대규모)
D) 제한 없음

[Answer]: C

---

### Question 3: 로깅 수준
MCP Tool 호출 로깅 수준은?

A) 최소 (에러만)
B) 표준 (요청/응답 요약)
C) 상세 (전체 페이로드 포함)

[Answer]: C

---

### Question 4: 재시도 정책
Backend API 호출 실패 시 재시도 정책은?

A) 재시도 없음 (즉시 에러 반환)
B) 1회 재시도
C) 3회 재시도 (exponential backoff)

[Answer]: C

---

## Design Steps

- [x] 성능 요구사항 정의
- [x] 확장성 요구사항 정의
- [x] 보안 요구사항 정의
- [x] 운영 요구사항 정의

---

답변을 완료하셨으면 알려주세요.
