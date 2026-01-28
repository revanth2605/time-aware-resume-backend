from data.db import users_collection
from werkzeug.security import generate_password_hash, check_password_hash


# ------------------------------------
# CREATE USER
# ------------------------------------

def create_user(username, password, role="user"):
    user = {
        "username": username,
        "password": generate_password_hash(password),
        "role": role
    }
    users_collection.insert_one(user)
    return user


# ------------------------------------
# GET USER BY USERNAME
# ------------------------------------

def get_user_by_username(username):
    return users_collection.find_one({"username": username})


# ------------------------------------
# VERIFY PASSWORD
# ------------------------------------

def verify_password(user, password):
    return check_password_hash(user["password"], password)
