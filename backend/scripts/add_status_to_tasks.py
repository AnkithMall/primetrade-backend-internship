import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.config import db

def add_status_to_tasks():
    db.tasks.update_many(
        {"status": {"$exists": False}},
        {"$set": {"status": "pending"}}
    )

if __name__ == "__main__":
    add_status_to_tasks()
