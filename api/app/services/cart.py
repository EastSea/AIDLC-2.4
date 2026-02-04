from sqlalchemy.orm import Session
from app.models import CartItem, Menu
from app.schemas.cart import CartItemCreate, CartItemUpdate, CartItemResponse, CartResponse
import uuid

class CartService:
    @staticmethod
    def get_cart(db: Session, session_id: str) -> CartResponse:
        items = db.query(CartItem).filter(CartItem.session_id == session_id).all()
        
        cart_items = []
        total = 0
        
        for item in items:
            menu = db.query(Menu).filter(Menu.id == item.menu_id).first()
            if menu:
                subtotal = menu.price * item.quantity
                cart_items.append(CartItemResponse(
                    id=item.id,
                    menu_id=item.menu_id,
                    menu_name=menu.name,
                    quantity=item.quantity,
                    unit_price=menu.price,
                    subtotal=subtotal,
                    options=item.options
                ))
                total += subtotal
        
        return CartResponse(session_id=session_id, items=cart_items, total=total)
    
    @staticmethod
    def add_to_cart(db: Session, cart_item: CartItemCreate) -> CartResponse:
        menu = db.query(Menu).filter(Menu.id == cart_item.menu_id).first()
        if not menu:
            raise ValueError("Menu not found")
        
        existing = db.query(CartItem).filter(
            CartItem.session_id == cart_item.session_id,
            CartItem.menu_id == cart_item.menu_id,
            CartItem.options == cart_item.options
        ).first()
        
        if existing:
            existing.quantity += cart_item.quantity
        else:
            new_item = CartItem(
                id=str(uuid.uuid4()),
                session_id=cart_item.session_id,
                menu_id=cart_item.menu_id,
                quantity=cart_item.quantity,
                options=cart_item.options
            )
            db.add(new_item)
        
        db.commit()
        return CartService.get_cart(db, cart_item.session_id)
    
    @staticmethod
    def update_cart_item(db: Session, item_id: str, update: CartItemUpdate) -> CartResponse:
        item = db.query(CartItem).filter(CartItem.id == item_id).first()
        if not item:
            raise ValueError("Cart item not found")
        
        item.quantity = update.quantity
        db.commit()
        
        return CartService.get_cart(db, item.session_id)
    
    @staticmethod
    def remove_cart_item(db: Session, item_id: str) -> CartResponse:
        item = db.query(CartItem).filter(CartItem.id == item_id).first()
        if not item:
            raise ValueError("Cart item not found")
        
        session_id = item.session_id
        db.delete(item)
        db.commit()
        
        return CartService.get_cart(db, session_id)
    
    @staticmethod
    def clear_cart(db: Session, session_id: str) -> bool:
        db.query(CartItem).filter(CartItem.session_id == session_id).delete()
        db.commit()
        return True
