from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.staff_call import StaffCallRequest, StaffCallResponse
from app.services.staff_call import StaffCallService

router = APIRouter(prefix="/api/customer/staff-call", tags=["customer-staff-call"])

@router.post("", response_model=StaffCallResponse)
def create_staff_call(request: StaffCallRequest, db: Session = Depends(get_db)):
    service = StaffCallService(db)
    call = service.create_call(request.table_id)
    return {"success": True, "call_id": call.id}
