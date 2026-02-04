# Unit 3 (MCP Servers) - TDD Code Generation Plan

## TDD Cycle: Red → Green → Refactor

### Phase 1: mcp-core
- [x] Models (ToolResponse, CustomerContext, AdminContext)
- [x] SessionManager (Redis)
- [x] TableOrderClient (httpx + retry)

### Phase 2: customer-mcp
- [x] Context Tool (set_table_context)
- [x] Menu Tools (get_categories, get_menus)
- [x] Cart Tools (add_to_cart, view_cart, place_order)
- [x] Order Tools (get_orders, call_staff)
- [x] MCP Server

### Phase 3: admin-mcp
- [x] Context Tool (set_admin_context)
- [x] Order Tools (get_orders, update_order_status)
- [x] Menu Tools (get_menus, update_menu)
- [x] Table Tools (complete_table)
- [x] MCP Server

### Phase 4: Integration
- [x] 전체 테스트 실행
- [x] requirements.txt 업데이트
