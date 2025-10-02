# app/crud/user.py
from app.config import db
from bson import ObjectId
import bcrypt

def create_user(name, email, password, role="user"):
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    user = {"name": name, "email": email, "password_hash": password_hash, "role": role}
    result = db.users.insert_one(user)
    user["_id"] = result.inserted_id
    return user

def get_user_by_email(email):
    return db.users.find_one({"email": email})
