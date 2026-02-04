from pydantic import BaseModel

class TableLoginRequest(BaseModel):
    store_code: str
    table_number: int
    password: str

class TableLoginResponse(BaseModel):
    token: str
    table_id: str
    session_id: str
    table_number: int

class AdminLoginRequest(BaseModel):
    store_code: str
    username: str
    password: str

class AdminLoginResponse(BaseModel):
    token: str
    store_id: str
    user_id: str
