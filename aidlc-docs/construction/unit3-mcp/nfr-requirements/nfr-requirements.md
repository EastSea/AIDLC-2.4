# Unit 3 (MCP Servers) - NFR Requirements

## 1. 성능 요구사항

| 항목 | 요구사항 | 비고 |
|------|----------|------|
| 응답 시간 | 1초 이내 | Backend 응답 포함 |
| API 타임아웃 | 800ms | Backend 호출 타임아웃 |
| Redis 타임아웃 | 100ms | 세션 조회/저장 |

### 1.1 구현 방안
- httpx AsyncClient 사용 (비동기 HTTP)
- Connection pooling 활성화
- Redis 연결 풀 사용

## 2. 확장성 요구사항

| 항목 | 요구사항 | 비고 |
|------|----------|------|
| 동시 세션 | 100개 이상 | MCP Server당 |
| 세션 TTL | 3600초 | Redis 자동 만료 |

### 2.1 구현 방안
- Async/await 기반 비동기 처리
- Redis 세션 저장 (메모리 부담 최소화)
- Stateless MCP Server 설계

## 3. 보안 요구사항

| 항목 | 요구사항 |
|------|----------|
| 토큰 저장 | Redis (메모리 노출 방지) |
| 민감 정보 로깅 | 마스킹 처리 |
| 세션 검증 | 모든 Tool 호출 시 |

### 3.1 구현 방안
- JWT 토큰은 Redis에만 저장
- 비밀번호, 토큰 로깅 시 마스킹
- 컨텍스트 미설정 시 명확한 에러 반환

## 4. 운영 요구사항

### 4.1 로깅
| 항목 | 내용 |
|------|------|
| 수준 | 상세 (전체 페이로드) |
| 포맷 | JSON structured logging |
| 내용 | Tool명, 파라미터, 응답, 소요시간, 에러 |

### 4.2 재시도 정책
| 항목 | 값 |
|------|-----|
| 최대 재시도 | 3회 |
| 전략 | Exponential backoff |
| 초기 대기 | 100ms |
| 최대 대기 | 1000ms |
| 재시도 대상 | 5xx 에러, 타임아웃, 연결 실패 |

### 4.3 에러 처리
```python
# 재시도 대상
RETRYABLE_ERRORS = [
    httpx.TimeoutException,
    httpx.ConnectError,
    httpx.HTTPStatusError  # 5xx only
]

# 재시도 제외
NON_RETRYABLE = [
    400,  # Bad Request
    401,  # Unauthorized
    403,  # Forbidden
    404,  # Not Found
]
```

## 5. 기술 스택 결정

| 구분 | 기술 | 버전 |
|------|------|------|
| Runtime | Python | 3.11+ |
| MCP SDK | mcp | latest |
| HTTP Client | httpx | 0.25+ |
| Redis Client | redis-py | 5.0+ |
| Logging | structlog | 23.0+ |
| Retry | tenacity | 8.0+ |
