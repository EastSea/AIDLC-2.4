from sqlalchemy.orm import Session
from app.models import Order, OrderItem, Menu, TableSession
from typing import List, Optional
from uuid import uuid4
from datetime import datetime

class OrderService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_order(self, session_id: str, items: List[dict]) -> Optional[Order]:
        session = self.db.query(TableSession).filter(TableSession.id == session_id).first()
        if not session:
            return None
        
        order_count = self.db.query(Order).count()
        order = Order(
            id=str(uuid4()),
            session_id=session_id,
            order_number=f"ORD-{order_count + 1:04d}",
            status="pending",
            total_amount=0,
            created_at=datetime.utcnow()
        )
        
        total = 0
        order_items = []
        for item_data in items:
            menu = self.db.query(Menu).filter(Menu.id == item_data["menu_id"]).first()
            if not menu:
                continue
            
            subtotal = menu.price * item_data["quantity"]
            total += subtotal
            
            order_item = OrderItem(
                id=str(uuid4()),
                order_id=order.id,
                menu_id=menu.id,
                menu_name=menu.name,
                quantity=item_data["quantity"],
                unit_price=menu.price,
                subtotal=subtotal
            )
            order_items.append(order_item)
        
        order.total_amount = total
        self.db.add(order)
        self.db.add_all(order_items)
        self.db.commit()
        self.db.refresh(order)
        
        return order
    
    def get_orders_by_session(self, session_id: str) -> List[Order]:
        return self.db.query(Order).filter(Order.session_id == session_id).all()
    
    def get_order(self, order_id: str) -> Optional[Order]:
        return self.db.query(Order).filter(Order.id == order_id).first()
    
    def update_order_status(self, order_id: str, status: str) -> Optional[Order]:
        order = self.db.query(Order).filter(Order.id == order_id).first()
        if order:
            order.status = status
            self.db.commit()
            self.db.refresh(order)
        return order
    
    def delete_order(self, order_id: str) -> bool:
        order = self.db.query(Order).filter(Order.id == order_id).first()
        if order:
            self.db.delete(order)
            self.db.commit()
            return True
        return False
