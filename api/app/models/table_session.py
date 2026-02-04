from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class TableSession(Base):
    __tablename__ = "table_sessions"
    
    id = Column(String, primary_key=True)
    table_id = Column(String, ForeignKey("tables.id"), nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)
    
    table = relationship("Table", back_populates="sessions")
    orders = relationship("Order", back_populates="session", cascade="all, delete-orphan")
    cart_items = relationship("CartItem", back_populates="session", cascade="all, delete-orphan")
