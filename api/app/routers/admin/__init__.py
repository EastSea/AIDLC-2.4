from fastapi import APIRouter
from .auth import router as auth_router
from .order import router as order_router
from .menu import router as menu_router
from .table import router as table_router
from .staff_call import router as staff_call_router

admin_router = APIRouter()
admin_router.include_router(auth_router)
admin_router.include_router(order_router)
admin_router.include_router(menu_router)
admin_router.include_router(table_router)
admin_router.include_router(staff_call_router)
