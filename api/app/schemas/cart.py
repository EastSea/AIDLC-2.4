from pydantic import BaseModel
from typing import Optional

class CartItemBase(BaseModel):
    menu_id: str
    quantity: int
    options: Optional[str] = None

class CartItemCreate(CartItemBase):
    session_id: str

class CartItemUpdate(BaseModel):
    quantity: int

class CartItemResponse(BaseModel):
    id: str
    menu_id: str
    menu_name: str
    quantity: int
    unit_price: int
    subtotal: int
    options: Optional[str] = None

    class Config:
        from_attributes = True

class CartResponse(BaseModel):
    session_id: str
    items: list[CartItemResponse]
    total: int

    class Config:
        from_attributes = True
