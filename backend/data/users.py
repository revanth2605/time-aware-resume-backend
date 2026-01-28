import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from data.db import users_collection


# ----------------------------------
# CHECK USERNAME EXISTS
# ----------------------------------

def username_exists(username):
    return users_collection.find_one({"username": username}) is not None


# ----------------------------------
# GENERATE USER ID
# ----------------------------------

def generate_user_id():
    last_user = users_collection.find_one(
        sort=[("created_at", -1)]
    )

    if not last_user:
        return "USR-100001"

    last_number = int(last_user["user_id"].split("-")[1])
    return f"USR-{last_number + 1:06d}"


# ----------------------------------
# CREATE USER (WITH PASSWORD)
# ----------------------------------

def create_user(username, password, role="user"):

    if username_exists(username):
        return None

    user_id = generate_user_id()

    hashed_password = generate_password_hash(password)

    user = {
        "user_id": user_id,
        "username": username,
        "password": hashed_password,   # ✅ STORED SECURELY
        "role": role,
        "created_at": datetime.datetime.now()
    }

    users_collection.insert_one(user)
    return user


# ----------------------------------
# VERIFY PASSWORD
# ----------------------------------

def verify_password(user, password):
    return check_password_hash(user["password"], password)


# ----------------------------------
# GETTERS
# ----------------------------------

def get_user_by_username(username):
    return users_collection.find_one({"username": username})


def get_user_by_id(user_id):
    return users_collection.find_one({"user_id": user_id})


def get_all_users():
    return list(users_collection.find())
