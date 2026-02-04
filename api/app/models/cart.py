from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class CartItem(Base):
    __tablename__ = "cart_items"
    
    id = Column(String, primary_key=True)
    session_id = Column(String, ForeignKey("table_sessions.id"), nullable=False)
    menu_id = Column(String, ForeignKey("menus.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    options = Column(String, nullable=True)
    
    session = relationship("TableSession", back_populates="cart_items")
    menu = relationship("Menu")
