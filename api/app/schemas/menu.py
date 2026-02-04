from pydantic import BaseModel
from typing import Optional

class MenuBase(BaseModel):
    name: str
    price: int
    description: Optional[str] = None
    serving_size: str = "all"
    display_order: int = 0
    is_available: bool = True

class MenuResponse(MenuBase):
    id: str
    category_id: str
    image_url: Optional[str] = None
    
    class Config:
        from_attributes = True
