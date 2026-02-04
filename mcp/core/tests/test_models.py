import pytest
from mcp_core.models import ToolResponse, CustomerContext, AdminContext


class TestToolResponse:
    def test_success_response(self):
        resp = ToolResponse(success=True, data={"id": 1}, error=None)
        assert resp.success is True
        assert resp.data == {"id": 1}
        assert resp.error is None

    def test_error_response(self):
        resp = ToolResponse(success=False, data=None, error="에러 발생")
        assert resp.success is False
        assert resp.data is None
        assert resp.error == "에러 발생"

    def test_to_dict(self):
        resp = ToolResponse(success=True, data={"id": 1}, error=None)
        d = resp.to_dict()
        assert d == {"success": True, "data": {"id": 1}, "error": None}


class TestCustomerContext:
    def test_create(self):
        ctx = CustomerContext(
            session_id="sess-123",
            store_code="STORE01",
            table_number=5,
            token="jwt-token",
            table_id=10
        )
        assert ctx.session_id == "sess-123"
        assert ctx.table_number == 5

    def test_to_dict(self):
        ctx = CustomerContext(
            session_id="sess-123",
            store_code="STORE01",
            table_number=5,
            token="jwt-token",
            table_id=10
        )
        d = ctx.to_dict()
        assert "session_id" in d
        assert "token" in d


class TestAdminContext:
    def test_create(self):
        ctx = AdminContext(
            session_id="admin-sess",
            username="admin",
            token="admin-jwt",
            store_id=1
        )
        assert ctx.username == "admin"
        assert ctx.store_id == 1
