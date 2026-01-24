from data.users import create_user

def register_user(username, role="user"):
    user = create_user(username, role)

    if user is None:
        return {
            "success": False,
            "message": "Username already exists"
        }

    return {
        "success": True,
        "user_id": user["user_id"],
        "role": user["role"]
    }
