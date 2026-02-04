from fastapi import APIRouter
from .auth import router as auth_router
from .category import router as category_router
from .menu import router as menu_router
from .cart import router as cart_router
from .order import router as order_router
from .staff_call import router as staff_call_router

customer_router = APIRouter()
customer_router.include_router(auth_router)
customer_router.include_router(category_router)
customer_router.include_router(menu_router)
customer_router.include_router(cart_router)
customer_router.include_router(order_router)
customer_router.include_router(staff_call_router)
