from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(String, primary_key=True)
    store_id = Column(String, ForeignKey("stores.id"), nullable=False)
    name = Column(String, nullable=False)
    display_order = Column(Integer, default=0)
    
    store = relationship("Store", back_populates="categories")
    menus = relationship("Menu", back_populates="category", cascade="all, delete-orphan")
