from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.staff_call import StaffCallDetail
from app.services.staff_call import StaffCallService
from app.dependencies import get_current_admin
from app.models import AdminUser
from typing import List, Optional

router = APIRouter(prefix="/api/admin/staff-calls", tags=["admin-staff-calls"])

@router.get("", response_model=List[StaffCallDetail])
def get_staff_calls(
    acknowledged: Optional[bool] = None,
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    service = StaffCallService(db)
    return service.get_calls(acknowledged)

@router.patch("/{call_id}/acknowledge")
def acknowledge_call(
    call_id: str,
    admin: AdminUser = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    service = StaffCallService(db)
    call = service.acknowledge_call(call_id)
    if not call:
        return {"success": False}
    return {"success": True}
