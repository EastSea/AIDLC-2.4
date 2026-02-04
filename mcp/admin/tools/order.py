from typing import Optional
import structlog

logger = structlog.get_logger()
NO_CONTEXT_ERROR = "컨텍스트가 설정되지 않았습니다. set_admin_context를 먼저 호출해주세요."


async def get_orders(client, session_manager, mcp_session_id: str, table_id: Optional[str] = None) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        orders = await client.get_all_orders(ctx["token"], table_id)
        return {"success": True, "data": orders, "error": None}
    except Exception as e:
        logger.error("get_orders_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}


async def update_order_status(client, session_manager, mcp_session_id: str, order_id: str, status: str) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        result = await client.update_order_status(ctx["token"], order_id, status)
        return {"success": True, "data": result, "error": None}
    except Exception as e:
        logger.error("update_order_status_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}
