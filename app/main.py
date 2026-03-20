from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, courses

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="LMS Backend API", version="1.0.0")

# Register routes
app.include_router(users.router)
app.include_router(courses.router)

@app.get("/")
def root():
    return {"message": "LMS API is running 🚀"}