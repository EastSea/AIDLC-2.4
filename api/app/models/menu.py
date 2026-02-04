from sqlalchemy import Column, String, Integer, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Menu(Base):
    __tablename__ = "menus"
    
    id = Column(String, primary_key=True)
    category_id = Column(String, ForeignKey("categories.id"), nullable=False)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(Text)
    serving_size = Column(String, default="all")
    display_order = Column(Integer, default=0)
    is_available = Column(Boolean, default=True)
    
    category = relationship("Category", back_populates="menus")
    image = relationship("MenuImage", back_populates="menu", uselist=False, cascade="all, delete-orphan")
    order_items = relationship("OrderItem", back_populates="menu")
