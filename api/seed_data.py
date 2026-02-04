"""
Initial data seeding script for development
Run this after database migration to populate test data
"""
from uuid import uuid4
from datetime import datetime
from app.database import SessionLocal
from app.models import Store, AdminUser, Table, Category, Menu
from app.auth import get_password_hash

def seed_data():
    db = SessionLocal()
    
    try:
        # Create store
        store_id = str(uuid4())
        store = Store(
            id=store_id,
            name="Test Restaurant",
            code="TEST001",
            created_at=datetime.utcnow()
        )
        db.add(store)
        
        # Create admin user (username: admin, password: admin123)
        admin = AdminUser(
            id=str(uuid4()),
            store_id=store_id,
            username="admin",
            password_hash=get_password_hash("admin123"),
            created_at=datetime.utcnow()
        )
        db.add(admin)
        
        # Create tables (table 1-5, password: 1234)
        for i in range(1, 6):
            table = Table(
                id=str(uuid4()),
                store_id=store_id,
                table_number=i,
                password_hash=get_password_hash("1234"),
                created_at=datetime.utcnow()
            )
            db.add(table)
        
        # Create categories
        categories = [
            {"id": "cat-1", "name": "세트메뉴", "order": 1},
            {"id": "cat-2", "name": "싱글플레터", "order": 2},
            {"id": "cat-3", "name": "스테이크", "order": 3},
            {"id": "cat-4", "name": "파스타", "order": 4},
            {"id": "cat-5", "name": "피자", "order": 5},
        ]
        
        for cat in categories:
            category = Category(
                id=cat["id"],
                store_id=store_id,
                name=cat["name"],
                display_order=cat["order"]
            )
            db.add(category)
        
        # Create menus
        menus = [
            {"id": "menu-1", "category_id": "cat-1", "name": "BBQ파티팩 2~3인 세트", "price": 68000, "desc": "BBQ 모듬 세트", "serving": "1-2", "order": 1},
            {"id": "menu-2", "category_id": "cat-1", "name": "안심 스테이크 2인 세트", "price": 54000, "desc": "안심 스테이크 세트", "serving": "1-2", "order": 2},
            {"id": "menu-3", "category_id": "cat-1", "name": "바비큐 폭립 파티 3~4인 세트", "price": 69000, "desc": "폭립 파티 세트", "serving": "3-4", "order": 3},
            {"id": "menu-4", "category_id": "cat-3", "name": "티본 스테이크", "price": 45000, "desc": "프리미엄 티본", "serving": "1-2", "order": 1},
            {"id": "menu-5", "category_id": "cat-4", "name": "까르보나라", "price": 18000, "desc": "크림 파스타", "serving": "all", "order": 1},
        ]
        
        for m in menus:
            menu = Menu(
                id=m["id"],
                category_id=m["category_id"],
                name=m["name"],
                price=m["price"],
                description=m["desc"],
                serving_size=m["serving"],
                display_order=m["order"],
                is_available=True
            )
            db.add(menu)
        
        db.commit()
        print("✅ Database seeded successfully!")
        print(f"Store Code: TEST001")
        print(f"Admin - username: admin, password: admin123")
        print(f"Tables 1-5 - password: 1234")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()
