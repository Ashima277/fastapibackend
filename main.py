from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import student_survey
from app.db.session import engine
from app.db.base_class import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Survey API",
    description="Backend API for managing student surveys",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_survey.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
