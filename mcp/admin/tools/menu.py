import structlog

logger = structlog.get_logger()
NO_CONTEXT_ERROR = "컨텍스트가 설정되지 않았습니다. set_admin_context를 먼저 호출해주세요."


async def get_menus(client, session_manager, mcp_session_id: str) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        menus = await client.get_menus_admin(ctx["token"])
        return {"success": True, "data": menus, "error": None}
    except Exception as e:
        logger.error("get_menus_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}


async def update_menu(client, session_manager, mcp_session_id: str, menu_id: str, data: dict) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        result = await client.update_menu(ctx["token"], menu_id, data)
        return {"success": True, "data": result, "error": None}
    except Exception as e:
        logger.error("update_menu_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}
