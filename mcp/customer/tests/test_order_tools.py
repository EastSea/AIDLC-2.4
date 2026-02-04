import pytest
from unittest.mock import AsyncMock
from tools.order import get_orders, call_staff


@pytest.fixture
def mock_client():
    return AsyncMock()


@pytest.fixture
def mock_session():
    sm = AsyncMock()
    sm.get_context.return_value = {"token": "jwt", "session_id": "sess-1", "table_id": "tbl-1"}
    return sm


@pytest.mark.asyncio
class TestOrderTools:
    async def test_get_orders(self, mock_client, mock_session):
        mock_client.get_orders.return_value = [{"id": "ord-1", "status": "pending"}]
        
        result = await get_orders(mock_client, mock_session, "mcp-sess")
        
        assert result["success"] is True
        assert len(result["data"]) == 1

    async def test_call_staff(self, mock_client, mock_session):
        mock_client.call_staff.return_value = {"success": True, "call_id": "call-1"}
        
        result = await call_staff(mock_client, mock_session, "mcp-sess")
        
        assert result["success"] is True
