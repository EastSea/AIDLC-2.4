import pytest
from unittest.mock import AsyncMock, patch
from mcp_core.client import TableOrderClient


@pytest.fixture
def client():
    return TableOrderClient("http://localhost:8000/api")


@pytest.mark.asyncio
class TestTableOrderClient:
    async def test_login(self, client):
        with patch.object(client, '_post', new_callable=AsyncMock) as mock:
            mock.return_value = {"token": "jwt", "table_id": 1, "session_id": "sess"}
            result = await client.login("STORE01", 5, "1234")
            assert result["token"] == "jwt"
            mock.assert_called_once()

    async def test_get_categories(self, client):
        with patch.object(client, '_get', new_callable=AsyncMock) as mock:
            mock.return_value = [{"id": 1, "name": "메인"}]
            result = await client.get_categories("jwt")
            assert len(result) == 1

    async def test_get_menus(self, client):
        with patch.object(client, '_get', new_callable=AsyncMock) as mock:
            mock.return_value = [{"id": 1, "name": "김치찌개"}]
            result = await client.get_menus("jwt", category_id="cat-1")
            assert len(result) == 1

    async def test_create_order(self, client):
        with patch.object(client, '_post', new_callable=AsyncMock) as mock:
            mock.return_value = {"order_id": "ord-1", "order_number": "A001"}
            result = await client.create_order("jwt", "sess-1", [{"menu_id": 1, "quantity": 2}])
            assert result["order_id"] == "ord-1"

    async def test_admin_login(self, client):
        with patch.object(client, '_post', new_callable=AsyncMock) as mock:
            mock.return_value = {"token": "admin-jwt", "store_id": 1}
            result = await client.admin_login("STORE01", "admin", "pass")
            assert result["token"] == "admin-jwt"

    async def test_update_order_status(self, client):
        with patch.object(client, '_patch', new_callable=AsyncMock) as mock:
            mock.return_value = {"success": True}
            result = await client.update_order_status("jwt", "ord-1", "preparing")
            assert result["success"] is True
