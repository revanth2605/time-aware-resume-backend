from flask import Blueprint, request
from auth.login import login_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")

    if not username:
        return {"error": "Username required"}, 400

    result = login_user(username)
    if not result["success"]:
        return result, 401

    return result
