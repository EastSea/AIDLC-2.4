import pytest
from unittest.mock import AsyncMock
from tools.context import set_admin_context


@pytest.fixture
def mock_client():
    return AsyncMock()


@pytest.fixture
def mock_session():
    return AsyncMock()


@pytest.mark.asyncio
class TestSetAdminContext:
    async def test_success(self, mock_client, mock_session):
        mock_client.admin_login.return_value = {
            "token": "admin-jwt",
            "store_id": 1,
            "user_id": "user-1"
        }
        
        result = await set_admin_context(
            mock_client, mock_session, "mcp-sess-1",
            "STORE01", "admin", "pass123"
        )
        
        assert result["success"] is True
        assert result["data"]["store_id"] == 1
        mock_session.save_context.assert_called_once()

    async def test_login_failure(self, mock_client, mock_session):
        mock_client.admin_login.side_effect = Exception("Invalid credentials")
        
        result = await set_admin_context(
            mock_client, mock_session, "mcp-sess-1",
            "STORE01", "admin", "wrong"
        )
        
        assert result["success"] is False
