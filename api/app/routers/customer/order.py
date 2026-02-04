from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.order import OrderCreateRequest, OrderCreateResponse, OrderResponse
from app.services.order import OrderService
from app.dependencies import get_current_table
from app.models import Table
from typing import List

router = APIRouter(prefix="/api/customer/orders", tags=["customer-orders"])

@router.post("", response_model=OrderCreateResponse, status_code=status.HTTP_201_CREATED)
def create_order(
    request: OrderCreateRequest,
    table: Table = Depends(get_current_table),
    db: Session = Depends(get_db)
):
    service = OrderService(db)
    items = [{"menu_id": item.menu_id, "quantity": item.quantity} for item in request.items]
    order = service.create_order(request.session_id, items)
    if not order:
        raise HTTPException(status_code=400, detail="Failed to create order")
    
    return {"order_id": order.id, "order_number": order.order_number}

@router.get("", response_model=List[OrderResponse])
def get_orders(
    session_id: str,
    table: Table = Depends(get_current_table),
    db: Session = Depends(get_db)
):
    service = OrderService(db)
    return service.get_orders_by_session(session_id)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: str,
    table: Table = Depends(get_current_table),
    db: Session = Depends(get_db)
):
    service = OrderService(db)
    order = service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
