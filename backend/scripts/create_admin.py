# scripts/create_admin.py
import os
from getpass import getpass
from pymongo import MongoClient
import bcrypt
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "assignment_db")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]

def create_admin():
    email = input("Admin email: ").strip()
    name = input("Admin name: ").strip()
    password = getpass("Password (hidden): ").strip()
    if db.users.find_one({"email": email}):
        print("User with that email already exists.")
        return

    pw_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    user = {
        "name": name,
        "email": email,
        "password_hash": pw_hash,
        "role": "admin",
    }
    res = db.users.insert_one(user)
    print("Admin created with id:", res.inserted_id)

if __name__ == "__main__":
    create_admin()
