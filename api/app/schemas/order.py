from pydantic import BaseModel
from typing import List
from datetime import datetime

class OrderItemBase(BaseModel):
    menu_id: str
    quantity: int

class OrderItemResponse(BaseModel):
    id: str
    menu_id: str
    menu_name: str
    quantity: int
    unit_price: int
    subtotal: int
    
    class Config:
        from_attributes = True

class OrderCreateRequest(BaseModel):
    session_id: str
    items: List[OrderItemBase]

class OrderCreateResponse(BaseModel):
    order_id: str
    order_number: str

class OrderResponse(BaseModel):
    id: str
    session_id: str
    order_number: str
    status: str
    total_amount: int
    created_at: datetime
    items: List[OrderItemResponse]
    
    class Config:
        from_attributes = True

class OrderStatusRequest(BaseModel):
    status: str
