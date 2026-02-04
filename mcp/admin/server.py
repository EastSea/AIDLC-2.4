import asyncio
import os
import uuid
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import redis.asyncio as redis

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'core'))
from mcp_core import TableOrderClient, SessionManager

from tools import (
    set_admin_context, get_orders, update_order_status,
    get_menus, update_menu, complete_table
)

API_URL = os.getenv("API_URL", "http://localhost:8000/api")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

server = Server("admin-mcp")
client = TableOrderClient(API_URL)
redis_client = None
session_manager = None


@server.list_tools()
async def list_tools():
    return [
        Tool(name="set_admin_context", description="관리자 컨텍스트 설정", inputSchema={
            "type": "object",
            "properties": {
                "store_code": {"type": "string"},
                "username": {"type": "string"},
                "password": {"type": "string"}
            },
            "required": ["store_code", "username", "password"]
        }),
        Tool(name="get_orders", description="주문 목록 조회", inputSchema={
            "type": "object",
            "properties": {"table_id": {"type": "string"}},
        }),
        Tool(name="update_order_status", description="주문 상태 변경", inputSchema={
            "type": "object",
            "properties": {
                "order_id": {"type": "string"},
                "status": {"type": "string", "enum": ["pending", "preparing", "ready", "completed"]}
            },
            "required": ["order_id", "status"]
        }),
        Tool(name="get_menus", description="메뉴 목록 조회", inputSchema={"type": "object", "properties": {}}),
        Tool(name="update_menu", description="메뉴 수정", inputSchema={
            "type": "object",
            "properties": {
                "menu_id": {"type": "string"},
                "name": {"type": "string"},
                "price": {"type": "integer"},
                "is_available": {"type": "boolean"}
            },
            "required": ["menu_id"]
        }),
        Tool(name="complete_table", description="테이블 이용 완료", inputSchema={
            "type": "object",
            "properties": {"table_id": {"type": "string"}},
            "required": ["table_id"]
        }),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    global session_manager
    mcp_session_id = arguments.pop("_mcp_session_id", str(uuid.uuid4()))
    
    handlers = {
        "set_admin_context": lambda: set_admin_context(client, session_manager, mcp_session_id, arguments["store_code"], arguments["username"], arguments["password"]),
        "get_orders": lambda: get_orders(client, session_manager, mcp_session_id, arguments.get("table_id")),
        "update_order_status": lambda: update_order_status(client, session_manager, mcp_session_id, arguments["order_id"], arguments["status"]),
        "get_menus": lambda: get_menus(client, session_manager, mcp_session_id),
        "update_menu": lambda: update_menu(client, session_manager, mcp_session_id, arguments["menu_id"], {k: v for k, v in arguments.items() if k != "menu_id"}),
        "complete_table": lambda: complete_table(client, session_manager, mcp_session_id, arguments["table_id"]),
    }
    
    result = await handlers[name]()
    return [TextContent(type="text", text=str(result))]


async def main():
    global redis_client, session_manager
    redis_client = redis.from_url(REDIS_URL)
    session_manager = SessionManager(redis_client)
    
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
