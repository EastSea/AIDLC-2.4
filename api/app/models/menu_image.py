from sqlalchemy import Column, String, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class MenuImage(Base):
    __tablename__ = "menu_images"
    
    id = Column(String, primary_key=True)
    menu_id = Column(String, ForeignKey("menus.id"), nullable=False, unique=True)
    image_data = Column(LargeBinary, nullable=False)
    content_type = Column(String, default="image/jpeg")
    
    menu = relationship("Menu", back_populates="image")
