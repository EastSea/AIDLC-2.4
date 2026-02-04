from typing import Any
import structlog

logger = structlog.get_logger()


async def set_table_context(
    client, session_manager, mcp_session_id: str,
    store_code: str, table_number: int, password: str
) -> dict:
    try:
        result = await client.login(store_code, table_number, password)
        
        context = {
            "store_code": store_code,
            "table_number": table_number,
            "token": result["token"],
            "table_id": result["table_id"],
            "session_id": result["session_id"]
        }
        await session_manager.save_context(mcp_session_id, context)
        
        logger.info("table_context_set", store_code=store_code, table_number=table_number)
        
        return {
            "success": True,
            "data": {"table_id": result["table_id"], "session_id": result["session_id"]},
            "error": None
        }
    except Exception as e:
        logger.error("table_context_failed", error=str(e))
        return {"success": False, "data": None, "error": str(e)}
