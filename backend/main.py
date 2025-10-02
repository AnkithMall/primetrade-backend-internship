# main.py
from fastapi import FastAPI
from app.routers import user, task
from fastapi.middleware.cors import CORSMiddleware
import os 
from dotenv import load_dotenv
load_dotenv()
origins = [
    "http://localhost:5173",  # your frontend
    "http://127.0.0.1:5173",
    os.getenv("FRONTEND_URL")
]

app = FastAPI(title="Backend Developer Assignment", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # needed for OPTIONS preflight
    allow_headers=["*"],
)

# Include routers
app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(task.router, prefix="/api/v1/tasks", tags=["Tasks"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
