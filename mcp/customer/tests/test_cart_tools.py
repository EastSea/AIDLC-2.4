import pytest
from unittest.mock import AsyncMock
from tools.cart import add_to_cart, view_cart, place_order


@pytest.fixture
def mock_client():
    return AsyncMock()


@pytest.fixture
def mock_session():
    sm = AsyncMock()
    sm.get_context.return_value = {"token": "jwt", "session_id": "sess-1"}
    return sm


@pytest.mark.asyncio
class TestCartTools:
    async def test_add_to_cart(self, mock_client, mock_session):
        mock_client.add_to_cart.return_value = {"items": [{"menu_id": "1", "quantity": 2}], "total": 20000}
        
        result = await add_to_cart(mock_client, mock_session, "mcp-sess", "menu-1", 2)
        
        assert result["success"] is True
        assert result["data"]["total"] == 20000

    async def test_view_cart(self, mock_client, mock_session):
        mock_client.get_cart.return_value = {"items": [], "total": 0}
        
        result = await view_cart(mock_client, mock_session, "mcp-sess")
        
        assert result["success"] is True

    async def test_place_order(self, mock_client, mock_session):
        mock_client.get_cart.return_value = {"items": [{"menu_id": "1", "quantity": 2}], "total": 20000}
        mock_client.create_order.return_value = {"order_id": "ord-1", "order_number": "A001"}
        
        result = await place_order(mock_client, mock_session, "mcp-sess")
        
        assert result["success"] is True
        assert result["data"]["order_id"] == "ord-1"

    async def test_place_order_empty_cart(self, mock_client, mock_session):
        mock_client.get_cart.return_value = {"items": [], "total": 0}
        
        result = await place_order(mock_client, mock_session, "mcp-sess")
        
        assert result["success"] is False
        assert "비어" in result["error"]
