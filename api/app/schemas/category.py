from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    display_order: int = 0

class CategoryResponse(CategoryBase):
    id: str
    
    class Config:
        from_attributes = True
