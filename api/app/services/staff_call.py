from sqlalchemy.orm import Session
from app.models import StaffCall
from typing import List, Optional
from uuid import uuid4
from datetime import datetime

class StaffCallService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_call(self, table_id: str) -> StaffCall:
        call = StaffCall(
            id=str(uuid4()),
            table_id=table_id,
            created_at=datetime.utcnow(),
            acknowledged=False
        )
        self.db.add(call)
        self.db.commit()
        self.db.refresh(call)
        return call
    
    def get_calls(self, acknowledged: Optional[bool] = None) -> List[StaffCall]:
        query = self.db.query(StaffCall)
        if acknowledged is not None:
            query = query.filter(StaffCall.acknowledged == acknowledged)
        return query.order_by(StaffCall.created_at.desc()).all()
    
    def acknowledge_call(self, call_id: str) -> Optional[StaffCall]:
        call = self.db.query(StaffCall).filter(StaffCall.id == call_id).first()
        if call:
            call.acknowledged = True
            call.acknowledged_at = datetime.utcnow()
            self.db.commit()
            self.db.refresh(call)
        return call
