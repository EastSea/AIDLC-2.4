from typing import Optional
import structlog

logger = structlog.get_logger()
NO_CONTEXT_ERROR = "컨텍스트가 설정되지 않았습니다. set_table_context를 먼저 호출해주세요."


async def add_to_cart(client, session_manager, mcp_session_id: str, menu_id: str, quantity: int, options: Optional[str] = None) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        cart = await client.add_to_cart(ctx["token"], ctx["session_id"], menu_id, quantity, options)
        return {"success": True, "data": cart, "error": None}
    except Exception as e:
        logger.error("add_to_cart_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}


async def view_cart(client, session_manager, mcp_session_id: str) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        cart = await client.get_cart(ctx["token"], ctx["session_id"])
        return {"success": True, "data": cart, "error": None}
    except Exception as e:
        logger.error("view_cart_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}


async def place_order(client, session_manager, mcp_session_id: str) -> dict:
    ctx = await session_manager.get_context(mcp_session_id)
    if not ctx:
        return {"success": False, "data": None, "error": NO_CONTEXT_ERROR}
    
    try:
        cart = await client.get_cart(ctx["token"], ctx["session_id"])
        if not cart.get("items"):
            return {"success": False, "data": None, "error": "장바구니가 비어있습니다."}
        
        order = await client.create_order(ctx["token"], ctx["session_id"], cart["items"])
        return {"success": True, "data": order, "error": None}
    except Exception as e:
        logger.error("place_order_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}
