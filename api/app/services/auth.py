from sqlalchemy.orm import Session
from app.models import Store, Table, AdminUser, TableSession
from app.auth import verify_password, create_access_token, get_password_hash
from uuid import uuid4
from datetime import datetime
from typing import Optional

class AuthService:
    def __init__(self, db: Session):
        self.db = db
    
    def table_login(self, store_code: str, table_number: int, password: str) -> Optional[dict]:
        store = self.db.query(Store).filter(Store.code == store_code).first()
        if not store:
            return None
        
        table = self.db.query(Table).filter(
            Table.store_id == store.id,
            Table.table_number == table_number
        ).first()
        if not table or not verify_password(password, table.password_hash):
            return None
        
        # Create new session
        session = TableSession(
            id=str(uuid4()),
            table_id=str(table.id),
            started_at=datetime.utcnow()
        )
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        
        token = create_access_token({"table_id": str(table.id), "type": "table"})
        
        return {
            "token": token,
            "table_id": str(table.id),
            "session_id": session.id,
            "table_number": table.table_number
        }
    
    def admin_login(self, store_code: str, username: str, password: str) -> Optional[dict]:
        store = self.db.query(Store).filter(Store.code == store_code).first()
        if not store:
            return None
        
        admin = self.db.query(AdminUser).filter(
            AdminUser.store_id == store.id,
            AdminUser.username == username
        ).first()
        if not admin or not verify_password(password, admin.password_hash):
            return None
        
        token = create_access_token({"user_id": str(admin.id), "store_id": str(store.id), "type": "admin"})
        
        return {
            "token": token,
            "store_id": str(store.id),
            "user_id": str(admin.id)
        }
