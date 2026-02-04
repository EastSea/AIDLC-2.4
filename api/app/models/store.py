from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(String, primary_key=True)
    name = Column(String(100), nullable=False)
    code = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime)
    
    tables = relationship("Table", back_populates="store")
    categories = relationship("Category", back_populates="store")
    admin_users = relationship("AdminUser", back_populates="store")
