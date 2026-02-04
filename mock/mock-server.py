"""Mock API Server for Table Order Service"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
from datetime import datetime

app = FastAPI(title="Table Order Mock API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock Data
CATEGORIES = [
    {"id": "cat-1", "name": "세트메뉴", "display_order": 1},
    {"id": "cat-2", "name": "싱글플레터", "display_order": 2},
    {"id": "cat-3", "name": "스테이크", "display_order": 3},
    {"id": "cat-4", "name": "파스타", "display_order": 4},
    {"id": "cat-5", "name": "피자", "display_order": 5},
]

MENUS = [
    {"id": "menu-1", "category_id": "cat-1", "name": "BBQ파티팩 2~3인 세트", "price": 68000, "description": "BBQ 모듬 세트", "serving_size": "1-2", "display_order": 1, "is_available": True, "image_url": "/api/customer/menus/menu-1/image"},
    {"id": "menu-2", "category_id": "cat-1", "name": "안심 스테이크 2인 세트", "price": 54000, "description": "안심 스테이크 세트", "serving_size": "1-2", "display_order": 2, "is_available": True, "image_url": None},
    {"id": "menu-3", "category_id": "cat-1", "name": "바비큐 폭립 파티 3~4인 세트", "price": 69000, "description": "폭립 파티 세트", "serving_size": "3-4", "display_order": 3, "is_available": True, "image_url": None},
    {"id": "menu-4", "category_id": "cat-3", "name": "티본 스테이크", "price": 45000, "description": "프리미엄 티본", "serving_size": "1-2", "display_order": 1, "is_available": True, "image_url": None},
    {"id": "menu-5", "category_id": "cat-4", "name": "까르보나라", "price": 18000, "description": "크림 파스타", "serving_size": "all", "display_order": 1, "is_available": True, "image_url": None},
]

ORDERS = []
STAFF_CALLS = []

# Request Models
class TableLoginRequest(BaseModel):
    store_code: str
    table_number: int
    password: str

class AdminLoginRequest(BaseModel):
    store_code: str
    username: str
    password: str

class OrderCreateRequest(BaseModel):
    session_id: str
    items: list

class StaffCallRequest(BaseModel):
    table_id: str

class OrderStatusRequest(BaseModel):
    status: str

# Customer Endpoints
@app.post("/api/customer/auth/login")
def customer_login(req: TableLoginRequest):
    return {"token": f"mock-token-{uuid4()}", "table_id": str(uuid4()), "session_id": str(uuid4()), "table_number": req.table_number}

@app.get("/api/customer/categories")
def get_categories():
    return CATEGORIES

@app.get("/api/customer/menus")
def get_menus(category_id: Optional[str] = None, serving_size: Optional[str] = None):
    result = MENUS
    if category_id:
        result = [m for m in result if m["category_id"] == category_id]
    if serving_size and serving_size != "all":
        result = [m for m in result if m["serving_size"] == serving_size or m["serving_size"] == "all"]
    return result

@app.get("/api/customer/menus/{menu_id}")
def get_menu(menu_id: str):
    menu = next((m for m in MENUS if m["id"] == menu_id), None)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menu

@app.get("/api/customer/orders")
def get_orders(session_id: str):
    return [o for o in ORDERS if o["session_id"] == session_id]

@app.post("/api/customer/orders", status_code=201)
def create_order(req: OrderCreateRequest):
    order_id = str(uuid4())
    order_number = f"ORD-{len(ORDERS)+1:04d}"
    items = []
    total = 0
    for item in req.items:
        menu = next((m for m in MENUS if m["id"] == item["menu_id"]), None)
        if menu:
            subtotal = menu["price"] * item["quantity"]
            total += subtotal
            items.append({"id": str(uuid4()), "menu_id": item["menu_id"], "menu_name": menu["name"], "quantity": item["quantity"], "unit_price": menu["price"], "subtotal": subtotal})
    order = {"id": order_id, "session_id": req.session_id, "order_number": order_number, "status": "pending", "total_amount": total, "created_at": datetime.now().isoformat(), "items": items}
    ORDERS.append(order)
    return {"order_id": order_id, "order_number": order_number}

@app.post("/api/customer/staff-call")
def staff_call(req: StaffCallRequest):
    call_id = str(uuid4())
    STAFF_CALLS.append({"id": call_id, "table_id": req.table_id, "created_at": datetime.now().isoformat(), "acknowledged": False})
    return {"success": True, "call_id": call_id}

# Admin Endpoints
@app.post("/api/admin/auth/login")
def admin_login(req: AdminLoginRequest):
    return {"token": f"mock-admin-token-{uuid4()}", "store_id": str(uuid4()), "user_id": str(uuid4())}

@app.get("/api/admin/orders")
def admin_get_orders(table_id: Optional[str] = None):
    return ORDERS

@app.patch("/api/admin/orders/{order_id}/status")
def update_order_status(order_id: str, req: OrderStatusRequest):
    order = next((o for o in ORDERS if o["id"] == order_id), None)
    if order:
        order["status"] = req.status
    return {"success": True}

@app.delete("/api/admin/orders/{order_id}")
def delete_order(order_id: str):
    global ORDERS
    ORDERS = [o for o in ORDERS if o["id"] != order_id]
    return {"success": True}

@app.post("/api/admin/tables/{table_id}/complete")
def complete_table(table_id: str):
    return {"success": True}

@app.get("/api/admin/menus")
def admin_get_menus():
    return MENUS

@app.get("/api/admin/staff-calls")
def get_staff_calls():
    return STAFF_CALLS

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
