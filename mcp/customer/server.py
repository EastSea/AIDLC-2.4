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
    set_table_context, get_categories, get_menus,
    add_to_cart, view_cart, place_order, get_orders, call_staff
)

API_URL = os.getenv("API_URL", "http://localhost:8000/api")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

server = Server("customer-mcp")
client = TableOrderClient(API_URL)
redis_client = None
session_manager = None


@server.list_tools()
async def list_tools():
    return [
        Tool(name="set_table_context", description="테이블 컨텍스트 설정", inputSchema={
            "type": "object",
            "properties": {
                "store_code": {"type": "string"},
                "table_number": {"type": "integer"},
                "password": {"type": "string"}
            },
            "required": ["store_code", "table_number", "password"]
        }),
        Tool(name="get_categories", description="카테고리 목록 조회", inputSchema={"type": "object", "properties": {}}),
        Tool(name="get_menus", description="메뉴 목록 조회", inputSchema={
            "type": "object",
            "properties": {"category_id": {"type": "string"}},
        }),
        Tool(name="add_to_cart", description="장바구니 추가", inputSchema={
            "type": "object",
            "properties": {
                "menu_id": {"type": "string"},
                "quantity": {"type": "integer"},
                "options": {"type": "string"}
            },
            "required": ["menu_id", "quantity"]
        }),
        Tool(name="view_cart", description="장바구니 조회", inputSchema={"type": "object", "properties": {}}),
        Tool(name="place_order", description="주문 생성", inputSchema={"type": "object", "properties": {}}),
        Tool(name="get_orders", description="주문 내역 조회", inputSchema={"type": "object", "properties": {}}),
        Tool(name="call_staff", description="직원 호출", inputSchema={"type": "object", "properties": {}}),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    global session_manager
    mcp_session_id = arguments.pop("_mcp_session_id", str(uuid.uuid4()))
    
    handlers = {
        "set_table_context": lambda: set_table_context(client, session_manager, mcp_session_id, arguments["store_code"], arguments["table_number"], arguments["password"]),
        "get_categories": lambda: get_categories(client, session_manager, mcp_session_id),
        "get_menus": lambda: get_menus(client, session_manager, mcp_session_id, arguments.get("category_id")),
        "add_to_cart": lambda: add_to_cart(client, session_manager, mcp_session_id, arguments["menu_id"], arguments["quantity"], arguments.get("options")),
        "view_cart": lambda: view_cart(client, session_manager, mcp_session_id),
        "place_order": lambda: place_order(client, session_manager, mcp_session_id),
        "get_orders": lambda: get_orders(client, session_manager, mcp_session_id),
        "call_staff": lambda: call_staff(client, session_manager, mcp_session_id),
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
