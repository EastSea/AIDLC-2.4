from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.auth import TableLoginRequest, TableLoginResponse
from app.services.auth import AuthService

router = APIRouter(prefix="/api/customer/auth", tags=["customer-auth"])

@router.post("/login", response_model=TableLoginResponse)
def login(request: TableLoginRequest, db: Session = Depends(get_db)):
    service = AuthService(db)
    result = service.table_login(request.store_code, request.table_number, request.password)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result
