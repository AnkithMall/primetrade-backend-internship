# app/routers/task.py
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.task import TaskCreate, TaskOut
from app.crud.task import create_task, get_tasks_by_owner, get_task_by_id, update_task, delete_task
from app.auth.dependencies import get_current_user, require_admin

router = APIRouter()

# Create Task
@router.post("/", response_model=TaskOut)
def create_task_route(task: TaskCreate, current_user=Depends(get_current_user)):
    db_task = create_task(task.title, task.description, current_user["_id"], task.status)
    return {
        "id": str(db_task["_id"]),
        "title": db_task["title"],
        "description": db_task["description"],
        "owner_id": str(db_task["owner_id"]),
        "status": db_task["status"]
    }

# Get My Tasks
@router.get("/", response_model=list[TaskOut])
def get_my_tasks(current_user=Depends(get_current_user)):
    tasks = get_tasks_by_owner(current_user["_id"])
    return [
        {
            "id": str(t["_id"]),
            "title": t["title"],
            "description": t["description"],
            "owner_id": str(t["owner_id"]),
            "status": t["status"]
        }
        for t in tasks
    ]

# Get Single Task (Owner or Admin)
@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: str, current_user=Depends(get_current_user)):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if str(task["owner_id"]) != str(current_user["_id"]) and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "owner_id": str(task["owner_id"]),
        "status": task["status"]
    }

# Update Task
@router.put("/{task_id}", response_model=TaskOut)
def update_task_route(task_id: str, task_data: TaskCreate, current_user=Depends(get_current_user)):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if str(task["owner_id"]) != str(current_user["_id"]) and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    updated_task = update_task(task_id, task_data.dict())
    return {
        "id": str(updated_task["_id"]),
        "title": updated_task["title"],
        "description": updated_task["description"],
        "owner_id": str(updated_task["owner_id"]),
        "status": updated_task["status"]
    }

# Delete Task
@router.delete("/{task_id}")
def delete_task_route(task_id: str, current_user=Depends(get_current_user)):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if str(task["owner_id"]) != str(current_user["_id"]) and current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    delete_task(task_id)
    return {"message": "Task deleted successfully"}
