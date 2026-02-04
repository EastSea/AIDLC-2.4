from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.order import OrderResponse, OrderStatusRequest
from app.services.order import OrderService
from app.dependencies import get_current_admin
from app.models import AdminUser, Order
from typing import List, Optional

router = APIRouter(prefix="/api/admin/orders", tags=["admin-orders"])

@router.get("", response_model=List[OrderResponse])
def get_orders(
    table_id: Optional[str] = None,
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    query = db.query(Order)
    if table_id:
        query = query.join(Order.session).filter(Order.session.has(table_id=table_id))
    return query.all()

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: str,
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    service = OrderService(db)
    order = service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.patch("/{order_id}/status")
def update_order_status(
    order_id: str,
    request: OrderStatusRequest,
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    service = OrderService(db)
    order = service.update_order_status(order_id, request.status)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"success": True}

@router.delete("/{order_id}")
def delete_order(
    order_id: str,
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    service = OrderService(db)
    success = service.delete_order(order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"success": True}

@router.get("/history")
def get_order_history(
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    return []
