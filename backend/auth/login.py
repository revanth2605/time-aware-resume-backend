from flask_jwt_extended import create_access_token
from data.users import get_user_by_username, verify_password


def login_user(username, password):

    user = get_user_by_username(username)

    if not user:
        return {
            "success": False,
            "message": "Invalid username"
        }

    # ✅ PASSWORD CHECK
    if not verify_password(user, password):
        return {
            "success": False,
            "message": "Invalid password"
        }

    token = create_access_token(
        identity=str(user["user_id"]),   # ✅ USE YOUR OWN USER ID
        additional_claims={
            "role": user["role"],
            "username": user["username"]
        }
    )

    return {
        "success": True,
        "access_token": token
    }
