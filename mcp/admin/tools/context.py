import structlog

logger = structlog.get_logger()


async def set_admin_context(
    client, session_manager, mcp_session_id: str,
    store_code: str, username: str, password: str
) -> dict:
    try:
        result = await client.admin_login(store_code, username, password)
        
        context = {
            "store_code": store_code,
            "username": username,
            "token": result["token"],
            "store_id": result["store_id"],
            "user_id": result.get("user_id")
        }
        await session_manager.save_context(mcp_session_id, context)
        
        logger.info("admin_context_set", store_code=store_code, username=username)
        
        return {
            "success": True,
            "data": {"store_id": result["store_id"], "user_id": result.get("user_id")},
            "error": None
        }
    except Exception as e:
        logger.error("admin_context_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}
