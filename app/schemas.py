from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from app.models import RoleEnum

# Employee schemas
class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: RoleEnum = RoleEnum.employee
    department_id: Optional[int] = None

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    role: RoleEnum
    department_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True

# Auth schemas
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: str
    name: str

# Course schemas
class CourseCreate(BaseModel):
    title: str
    description: Optional[str] = None

class CourseResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_published: bool
    created_at: datetime

    class Config:
        from_attributes = True