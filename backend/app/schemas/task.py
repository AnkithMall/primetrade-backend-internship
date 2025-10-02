# app/schemas/task.py
from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "pending"

class TaskOut(BaseModel):
    id: str
    title: str
    description: Optional[str]
    owner_id: str
    status: str
