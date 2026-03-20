from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, courses
from app.routes import auth as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Company LMS API", version="1.0.0")

app.include_router(auth_router.router)
app.include_router(users.router)
app.include_router(courses.router)

@app.get("/")
def root():
    return {"message": "Company LMS API is running 🚀"}