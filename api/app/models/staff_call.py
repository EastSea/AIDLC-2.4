from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class StaffCall(Base):
    __tablename__ = "staff_calls"
    
    id = Column(String, primary_key=True)
    table_id = Column(String, ForeignKey("tables.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    acknowledged = Column(Boolean, default=False)
    acknowledged_at = Column(DateTime, nullable=True)
    
    table = relationship("Table", back_populates="staff_calls")
