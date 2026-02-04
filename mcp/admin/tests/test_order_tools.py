import pytest
from unittest.mock import AsyncMock
from tools.order import get_orders, update_order_status


@pytest.fixture
def mock_client():
    return AsyncMock()


@pytest.fixture
def mock_session():
    sm = AsyncMock()
    sm.get_context.return_value = {"token": "admin-jwt", "store_id": 1}
    return sm


@pytest.mark.asyncio
class TestAdminOrderTools:
    async def test_get_orders(self, mock_client, mock_session):
        mock_client.get_all_orders.return_value = [{"id": "ord-1", "status": "pending"}]
        
        result = await get_orders(mock_client, mock_session, "mcp-sess")
        
        assert result["success"] is True
        assert len(result["data"]) == 1

    async def test_get_orders_no_context(self, mock_client, mock_session):
        mock_session.get_context.return_value = None
        
        result = await get_orders(mock_client, mock_session, "mcp-sess")
        
        assert result["success"] is False

    async def test_update_order_status(self, mock_client, mock_session):
        mock_client.update_order_status.return_value = {"success": True}
        
        result = await update_order_status(mock_client, mock_session, "mcp-sess", "ord-1", "preparing")
        
        assert result["success"] is True
