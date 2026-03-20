from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Course
from app.schemas import CourseCreate, CourseResponse
from app.dependencies import require_hr_admin, require_employee  # ← import guards

router = APIRouter(prefix="/courses", tags=["Courses"])

# Only HR admin can create course
@router.post("/", response_model=CourseResponse)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db),
    current=Depends(require_hr_admin)  # ← HR guard
):
    new_course = Course(title=course.title, description=course.description)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

# All employees can view courses
@router.get("/", response_model=list[CourseResponse])
def get_courses(
    db: Session = Depends(get_db),
    current=Depends(require_employee)  # ← employee guard
):
    return db.query(Course).all()

# All employees can view single course
@router.get("/{course_id}", response_model=CourseResponse)
def get_course(
    course_id: int,
    db: Session = Depends(get_db),
    current=Depends(require_employee)  # ← employee guard
):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

# Only HR admin can delete course
@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
    current=Depends(require_hr_admin)  # ← HR guard
):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return {"message": "Course deleted"}