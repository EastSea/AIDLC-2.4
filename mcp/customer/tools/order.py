import structlog

logger = structlog.get_logger()
NO_CONTEXT_ERROR = "컨텍스트가 설정되지 않았습니다. set_table_context를 먼저 호출해주세요."


async def get_orders(client, session_manager, mcp_session_id: str) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        orders = await client.get_orders(ctx["token"], ctx["session_id"])
        return {"success": True, "data": orders, "error": None}
    except Exception as e:
        logger.error("get_orders_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}


async def call_staff(client, session_manager, mcp_session_id: str) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        result = await client.call_staff(ctx["token"], ctx["table_id"])
        return {"success": True, "data": result, "error": None}
    except Exception as e:
        logger.error("call_staff_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}
