from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class StaffCallRequest(BaseModel):
    table_id: str

class StaffCallResponse(BaseModel):
    success: bool
    call_id: str

class StaffCallDetail(BaseModel):
    id: str
    table_id: str
    created_at: datetime
    acknowledged: bool
    acknowledged_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
