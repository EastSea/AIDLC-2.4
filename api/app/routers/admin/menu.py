from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.menu import MenuResponse
from app.services.menu import MenuService
from app.dependencies import get_current_admin
from app.models import AdminUser
from typing import List

router = APIRouter(prefix="/api/admin/menus", tags=["admin-menus"])

@router.get("", response_model=List[MenuResponse])
def get_menus(
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    service = MenuService(db)
    menus = service.get_menus(str(admin.store_id))
    
    result = []
    for menu in menus:
        menu_dict = {
            "id": menu.id,
            "category_id": menu.category_id,
            "name": menu.name,
            "price": menu.price,
            "description": menu.description,
            "serving_size": menu.serving_size,
            "display_order": menu.display_order,
            "is_available": menu.is_available,
            "image_url": f"/api/customer/menus/{menu.id}/image" if menu.image else None
        }
        result.append(menu_dict)
    
    return result
