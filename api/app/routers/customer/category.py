from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from app.schemas.category import CategoryResponse
from app.services.menu import MenuService
from typing import List

router = APIRouter(prefix="/api/customer/categories", tags=["customer-categories"])

@router.get("", response_model=List[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    service = MenuService(db)
    result = db.execute(text("SELECT id FROM stores LIMIT 1")).fetchone()
    store_id = result[0] if result else "store-1"
    return service.get_categories(store_id)
