from typing import Optional
import structlog

logger = structlog.get_logger()
NO_CONTEXT_ERROR = "컨텍스트가 설정되지 않았습니다. set_table_context를 먼저 호출해주세요."


async def get_categories(client, session_manager, mcp_session_id: str) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        categories = await client.get_categories(ctx["token"])
        return {"success": True, "data": categories, "error": None}
    except Exception as e:
        logger.error("get_categories_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}


async def get_menus(client, session_manager, mcp_session_id: str, category_id: Optional[str] = None) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        menus = await client.get_menus(ctx["token"], category_id)
        return {"success": True, "data": menus, "error": None}
    except Exception as e:
        logger.error("get_menus_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}
