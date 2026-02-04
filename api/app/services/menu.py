from sqlalchemy.orm import Session
from app.models import Category, Menu, MenuImage
from typing import List, Optional

class MenuService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_categories(self, store_id: str) -> List[Category]:
        return self.db.query(Category).filter(
            Category.store_id == store_id
        ).order_by(Category.display_order).all()
    
    def get_menus(
        self,
        store_id: str,
        category_id: Optional[str] = None,
        serving_size: Optional[str] = None
    ) -> List[Menu]:
        query = self.db.query(Menu).join(Category).filter(
            Category.store_id == store_id,
            Menu.is_available == True
        )
        
        if category_id:
            query = query.filter(Menu.category_id == category_id)
        
        if serving_size and serving_size != "all":
            query = query.filter(
                (Menu.serving_size == serving_size) | (Menu.serving_size == "all")
            )
        
        return query.order_by(Menu.display_order).all()
    
    def get_menu(self, menu_id: str) -> Optional[Menu]:
        return self.db.query(Menu).filter(Menu.id == menu_id).first()
    
    def get_menu_image(self, menu_id: str) -> Optional[MenuImage]:
        return self.db.query(MenuImage).filter(MenuImage.menu_id == menu_id).first()
