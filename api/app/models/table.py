from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Table(Base):
    __tablename__ = "tables"

    id = Column(String, primary_key=True)
    store_id = Column(String, ForeignKey("stores.id"), nullable=False)
    table_number = Column(Integer, nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime)
    
    store = relationship("Store", back_populates="tables")
    sessions = relationship("TableSession", back_populates="table")
    staff_calls = relationship("StaffCall", back_populates="table")
