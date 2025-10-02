from app.config import db
from bson import ObjectId
from datetime import datetime, timezone

def create_task(title, description, owner_id, status):
    task = {
        "title": title,
        "description": description,
        "owner_id": ObjectId(owner_id),
        "status": status,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc)
    }
    result = db.tasks.insert_one(task)
    task["_id"] = result.inserted_id
    return task

def get_tasks_by_owner(owner_id):
    return list(db.tasks.find({"owner_id": ObjectId(owner_id)}))

def get_task_by_id(task_id):
    return db.tasks.find_one({"_id": ObjectId(task_id)})

def update_task(task_id, data):
    return db.tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {**data, "updated_at": datetime.now(timezone.utc)}}
    )
    return db.tasks.find_one({"_id": ObjectId(task_id)})

def delete_task(task_id):
    return db.tasks.delete_one({"_id": ObjectId(task_id)})
