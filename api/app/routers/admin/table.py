from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Table, AdminUser
from app.dependencies import get_current_admin

router = APIRouter(prefix="/api/admin/tables", tags=["admin-tables"])

@router.get("")
def get_tables(
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    tables = db.query(Table).filter(Table.store_id == admin.store_id).all()
    return tables

@router.get("/{table_id}")
def get_table(
    table_id: str,
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    table = db.query(Table).filter(Table.id == table_id).first()
    return table

@router.post("/{table_id}/complete")
def complete_table(
    table_id: str,
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    return {"success": True}

@router.get("/{table_id}/summary")
def get_table_summary(
    table_id: str,
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    return {}
