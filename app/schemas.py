from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from app.models import RoleEnum

# ── Employee schemas ──────────────────────────
class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: RoleEnum = RoleEnum.employee
    department_id: Optional[int] = None

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[RoleEnum] = None
    department_id: Optional[int] = None
    is_active: Optional[bool] = None

class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    role: RoleEnum
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# ── Auth schemas ──────────────────────────────
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    role: str
    name: str

# ── Department schemas ────────────────────────
class DepartmentCreate(BaseModel):
    name: str

class DepartmentUpdate(BaseModel):
    name: Optional[str] = None

class DepartmentResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True

class DepartmentWithEmployees(BaseModel):
    id: int
    name: str
    created_at: datetime
    employees: List[EmployeeResponse] = []

    class Config:
        from_attributes = True

# ── Lesson schemas ────────────────────────────
class LessonCreate(BaseModel):
    title: str
    description: Optional[str] = None
    video_url: Optional[str] = None
    pdf_url: Optional[str] = None
    order: Optional[int] = 0
    duration_minutes: Optional[int] = None

class LessonUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    video_url: Optional[str] = None
    pdf_url: Optional[str] = None
    order: Optional[int] = None
    duration_minutes: Optional[int] = None

class LessonResponse(BaseModel):
    id: int
    course_id: int
    title: str
    description: Optional[str]
    video_url: Optional[str]
    pdf_url: Optional[str]
    order: int
    duration_minutes: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True

# ── Course schemas ────────────────────────────
class CourseCreate(BaseModel):
    title: str
    description: Optional[str] = None
    thumbnail_url: Optional[str] = None

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    thumbnail_url: Optional[str] = None

class CourseResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    thumbnail_url: Optional[str]
    is_published: bool
    created_at: datetime

    class Config:
        from_attributes = True

class CourseWithLessons(BaseModel):
    id: int
    title: str
    description: Optional[str]
    thumbnail_url: Optional[str]
    is_published: bool
    created_at: datetime
    lessons: List[LessonResponse] = []

    class Config:
        from_attributes = True