from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.cart import CartService
from app.schemas.cart import CartItemCreate, CartItemUpdate, CartResponse

router = APIRouter(prefix="/api/customer/cart", tags=["Customer Cart"])

@router.get("", response_model=CartResponse)
def get_cart(session_id: str, db: Session = Depends(get_db)):
    return CartService.get_cart(db, session_id)

@router.post("", response_model=CartResponse)
def add_to_cart(cart_item: CartItemCreate, db: Session = Depends(get_db)):
    try:
        return CartService.add_to_cart(db, cart_item)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/{item_id}", response_model=CartResponse)
def update_cart_item(item_id: str, update: CartItemUpdate, db: Session = Depends(get_db)):
    try:
        return CartService.update_cart_item(db, item_id, update)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{item_id}", response_model=CartResponse)
def remove_cart_item(item_id: str, db: Session = Depends(get_db)):
    try:
        return CartService.remove_cart_item(db, item_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("", response_model=dict)
def clear_cart(session_id: str, db: Session = Depends(get_db)):
    CartService.clear_cart(db, session_id)
    return {"success": True}
