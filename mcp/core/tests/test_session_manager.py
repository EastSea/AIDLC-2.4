import pytest
from unittest.mock import AsyncMock, MagicMock
from mcp_core.session_manager import SessionManager


@pytest.fixture
def mock_redis():
    redis = AsyncMock()
    return redis


@pytest.mark.asyncio
class TestSessionManager:
    async def test_save_context(self, mock_redis):
        sm = SessionManager(mock_redis)
        await sm.save_context("sess-123", {"token": "abc"})
        mock_redis.setex.assert_called_once()

    async def test_get_context(self, mock_redis):
        mock_redis.get.return_value = '{"token": "abc"}'
        sm = SessionManager(mock_redis)
        ctx = await sm.get_context("sess-123")
        assert ctx == {"token": "abc"}

    async def test_get_context_not_found(self, mock_redis):
        mock_redis.get.return_value = None
        sm = SessionManager(mock_redis)
        ctx = await sm.get_context("sess-123")
        assert ctx is None

    async def test_delete_context(self, mock_redis):
        sm = SessionManager(mock_redis)
        await sm.delete_context("sess-123")
        mock_redis.delete.assert_called_once_with("mcp:sess-123")

    async def test_is_valid(self, mock_redis):
        mock_redis.exists.return_value = 1
        sm = SessionManager(mock_redis)
        assert await sm.is_valid("sess-123") is True

    async def test_is_invalid(self, mock_redis):
        mock_redis.exists.return_value = 0
        sm = SessionManager(mock_redis)
        assert await sm.is_valid("sess-123") is False
