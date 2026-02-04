import pytest
from unittest.mock import AsyncMock
from tools.menu import get_categories, get_menus


@pytest.fixture
def mock_client():
    return AsyncMock()


@pytest.fixture
def mock_session():
    sm = AsyncMock()
    sm.get_context.return_value = {"token": "jwt", "session_id": "sess-1"}
    return sm


@pytest.mark.asyncio
class TestMenuTools:
    async def test_get_categories(self, mock_client, mock_session):
        mock_client.get_categories.return_value = [{"id": "1", "name": "메인"}]
        
        result = await get_categories(mock_client, mock_session, "mcp-sess")
        
        assert result["success"] is True
        assert len(result["data"]) == 1

    async def test_get_categories_no_context(self, mock_client, mock_session):
        mock_session.get_context.return_value = None
        
        result = await get_categories(mock_client, mock_session, "mcp-sess")
        
        assert result["success"] is False
        assert "컨텍스트" in result["error"]

    async def test_get_menus(self, mock_client, mock_session):
        mock_client.get_menus.return_value = [{"id": "1", "name": "김치찌개"}]
        
        result = await get_menus(mock_client, mock_session, "mcp-sess", "cat-1")
        
        assert result["success"] is True
        assert len(result["data"]) == 1
