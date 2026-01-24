from flask_jwt_extended import create_access_token
from data.users import get_user_by_username

def login_user(username):
    user = get_user_by_username(username)

    if not user:
        return {
            "success": False,
            "message": "Invalid username"
        }

    token = create_access_token(
        identity=str(user["user_id"]),   # ✅ MUST be string
        additional_claims={              # ✅ extra data goes here
            "role": user["role"],
            "username": user["username"]
        }
    )

    return {
        "success": True,
        "access_token": token
    }
