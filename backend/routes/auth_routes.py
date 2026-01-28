from flask import Blueprint, request
from auth.login import login_user
from auth.register import register_user

auth_bp = Blueprint("auth", __name__)

# ---------------------------
# LOGIN
# ---------------------------

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "Username and password required"}, 400

    result = login_user(username, password)

    if not result["success"]:
        return result, 401

    return result


# ---------------------------
# REGISTER
# ---------------------------

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "Username and password required"}, 400

    result = register_user(username, password)

    if not result["success"]:
        return result, 400

    return result
