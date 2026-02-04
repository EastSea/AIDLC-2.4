from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.category import CategoryResponse
from app.services.menu import MenuService
from app.dependencies import get_current_table
from app.models import Table
from typing import List

router = APIRouter(prefix="/api/customer/categories", tags=["customer-categories"])

@router.get("", response_model=List[CategoryResponse])
def get_categories(
    table: Table = Depends(get_current_table),
    db: Session = Depends(get_db)
):
    service = MenuService(db)
    return service.get_categories(str(table.store_id))
