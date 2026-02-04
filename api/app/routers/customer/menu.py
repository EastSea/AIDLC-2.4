from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from app.schemas.menu import MenuResponse
from app.services.menu import MenuService
from typing import List, Optional

router = APIRouter(prefix="/api/customer/menus", tags=["customer-menus"])

@router.get("", response_model=List[MenuResponse])
def get_menus(
    category_id: Optional[str] = None,
    serving_size: Optional[str] = None,
    db: Session = Depends(get_db)
):
    result = db.execute(text("SELECT id FROM stores LIMIT 1")).fetchone()
    store_id = result[0] if result else "store-1"
    service = MenuService(db)
    menus = service.get_menus(store_id, category_id, serving_size)
    
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

@router.get("/{menu_id}", response_model=MenuResponse)
def get_menu(menu_id: str, db: Session = Depends(get_db)):
    service = MenuService(db)
    menu = service.get_menu(menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    
    return {
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

@router.get("/{menu_id}/image")
def get_menu_image(menu_id: str, db: Session = Depends(get_db)):
    service = MenuService(db)
    image = service.get_menu_image(menu_id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    return Response(content=image.image_data, media_type=image.content_type)
