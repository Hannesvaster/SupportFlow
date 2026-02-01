from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TicketCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str = "normal"

class TicketOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    owner_id: Optional[int]

    class Config:
        from_attributes = True
