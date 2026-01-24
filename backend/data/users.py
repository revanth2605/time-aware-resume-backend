import datetime
from data.db import users_collection


def username_exists(username):
    return users_collection.find_one({"username": username}) is not None


def generate_user_id():
    last_user = users_collection.find_one(
        sort=[("created_at", -1)]
    )

    if not last_user:
        return "USR-100001"

    last_number = int(last_user["user_id"].split("-")[1])
    return f"USR-{last_number + 1:06d}"


def create_user(username, role="user"):
    if username_exists(username):
        return None

    user_id = generate_user_id()

    user = {
        "user_id": user_id,
        "username": username,
        "role": role,
        "created_at": datetime.datetime.now()
    }

    users_collection.insert_one(user)
    return user


def get_user_by_username(username):
    return users_collection.find_one({"username": username})


def get_user_by_id(user_id):
    return users_collection.find_one({"user_id": user_id})
def get_all_users():
    return list(users_collection.find())
