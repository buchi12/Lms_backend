from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Employee
from app.schemas import EmployeeCreate, LoginRequest, TokenResponse, EmployeeResponse
from app.auth import hash_password, verify_password, create_access_token
from app.dependencies import get_current_employee

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=EmployeeResponse)
def register(employee: EmployeeCreate, db: Session = Depends(get_db)):
    existing = db.query(Employee).filter(Employee.email == employee.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_employee = Employee(
        name=employee.name,
        email=employee.email,
        hashed_password=hash_password(employee.password),
        role=employee.role,
        department_id=employee.department_id
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.email == request.email).first()
    if not employee or not verify_password(request.password, employee.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token({"sub": employee.email, "role": employee.role})
    return {
        "access_token": token,
        "token_type": "bearer",
        "role": employee.role,
        "name": employee.name
    }

@router.get("/me", response_model=EmployeeResponse)
def get_me(current: Employee = Depends(get_current_employee)):
    return current