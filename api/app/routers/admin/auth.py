from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.auth import AdminLoginRequest, AdminLoginResponse
from app.services.auth import AuthService

router = APIRouter(prefix="/api/admin/auth", tags=["admin-auth"])

@router.post("/login", response_model=AdminLoginResponse)
def admin_login(request: AdminLoginRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    result = service.admin_login(request.store_code, request.username, request.password)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result

@router.post("/logout")
def admin_logout():
    return {"success": True}
