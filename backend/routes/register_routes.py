from flask import Blueprint, request
from data.users import create_user

register_bp = Blueprint("register", __name__)


@register_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")

    if not username:
        return {"error": "Username required"}, 400

    user = create_user(username)

    if not user:
        return {"error": "Username already exists"}, 409

    return {
        "message": "User registered successfully",
        "user_id": user["user_id"]
    }
