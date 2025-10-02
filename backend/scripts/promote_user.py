from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB_NAME", "primetrade")]

def promote_user(identifier: str):
    # You can search by email or ObjectId
    query = {"email": identifier} if "@" in identifier else {"_id": ObjectId(identifier)}

    res = db.users.update_one(query, {"$set": {"role": "admin"}})

    if res.matched_count == 0:
        print("❌ User not found")
    elif res.modified_count == 1:
        print("✅ User promoted to admin")
    else:
        print("ℹ️ User already admin")

if __name__ == "__main__":
    user_identifier = input("Enter user email or ObjectId: ").strip()
    promote_user(user_identifier)
