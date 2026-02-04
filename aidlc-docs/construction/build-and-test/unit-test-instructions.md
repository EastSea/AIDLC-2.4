# Unit Test Instructions

## MCP Core Tests

```bash
cd mcp/core
pip install -r requirements.txt
pytest tests/ -v
```

### 테스트 항목
- `test_models.py`: ToolResponse, CustomerContext, AdminContext
- `test_session_manager.py`: Redis 세션 CRUD
- `test_client.py`: TableOrderClient API 호출

## Customer MCP Tests

```bash
cd mcp/customer
pip install -r requirements.txt
pytest tests/ -v
```

### 테스트 항목
- `test_context_tools.py`: set_table_context
- `test_menu_tools.py`: get_categories, get_menus
- `test_cart_tools.py`: add_to_cart, view_cart, place_order
- `test_order_tools.py`: get_orders, call_staff

## Admin MCP Tests

```bash
cd mcp/admin
pip install -r requirements.txt
pytest tests/ -v
```

### 테스트 항목
- `test_context_tools.py`: set_admin_context
- `test_order_tools.py`: get_orders, update_order_status

## 전체 테스트 실행

```bash
# 프로젝트 루트에서
cd mcp/core && pytest tests/ -v
cd ../customer && pytest tests/ -v
cd ../admin && pytest tests/ -v
```

## Coverage 리포트

```bash
pip install pytest-cov
pytest tests/ --cov=. --cov-report=html
```
