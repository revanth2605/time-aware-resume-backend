import os
from pymongo import MongoClient
from urllib.parse import quote_plus

USERNAME = os.getenv("revanth")
PASSWORD = os.getenv("revanth12@")
HOST = os.getenv("cluster0.y5ewexh.mongodb.net")

# 🔴 HARD FAIL WITH CLEAR ERROR (instead of cryptic TypeError)
if not USERNAME or not PASSWORD or not HOST:
    raise RuntimeError(
        f"Missing MongoDB env vars: "
        f"MONGO_USERNAME={USERNAME}, "
        f"MONGO_PASSWORD={'SET' if PASSWORD else None}, "
        f"MONGO_HOST={HOST}"
    )

encoded_username = quote_plus(str(USERNAME))
encoded_password = quote_plus(str(PASSWORD))

MONGO_URI = (
    f"mongodb+srv://{encoded_username}:{encoded_password}"
    f"@{HOST}/?retryWrites=true&w=majority"
)

client = MongoClient(MONGO_URI)

db = client["time_aware_resume"]

users_collection = db["users"]
skills_collection = db["skills"]
activities_collection = db["activities"]
admin_flags_collection = db["admin_flags"]
