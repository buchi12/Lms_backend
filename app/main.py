from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth as auth_router
from app.routes import courses, departments, employees, uploads

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Company LMS API",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True}
)

app.include_router(auth_router.router)
app.include_router(employees.router)
app.include_router(departments.router)
app.include_router(courses.router)
app.include_router(uploads.router)

@app.get("/")
def root():
    return {"message": "Company LMS API is running 🚀"}