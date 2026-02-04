import structlog

logger = structlog.get_logger()
NO_CONTEXT_ERROR = "컨텍스트가 설정되지 않았습니다. set_admin_context를 먼저 호출해주세요."


async def complete_table(client, session_manager, mcp_session_id: str, table_id: str) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        result = await client.complete_table(ctx["token"], table_id)
        return {"success": True, "data": result, "error": None}
    except Exception as e:
        logger.error("complete_table_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}
