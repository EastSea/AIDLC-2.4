import pytest
from unittest.mock import AsyncMock, MagicMock
import sys
sys.path.insert(0, '../../core')

from tools.context import set_table_context


@pytest.fixture
def mock_client():
    return AsyncMock()


@pytest.fixture
def mock_session():
    return AsyncMock()


@pytest.mark.asyncio
class TestSetTableContext:
    async def test_success(self, mock_client, mock_session):
        mock_client.login.return_value = {
            "token": "jwt-token",
            "table_id": "tbl-1",
            "session_id": "sess-1"
        }
        
        result = await set_table_context(
            mock_client, mock_session, "mcp-sess-1",
            "STORE01", 5, "1234"
        )
        
        assert result["success"] is True
        assert result["data"]["table_id"] == "tbl-1"
        mock_session.save_context.assert_called_once()

    async def test_login_failure(self, mock_client, mock_session):
        mock_client.login.side_effect = Exception("Login failed")
        
        result = await set_table_context(
            mock_client, mock_session, "mcp-sess-1",
            "STORE01", 5, "wrong"
        )
        
        assert result["success"] is False
        assert "error" in result
