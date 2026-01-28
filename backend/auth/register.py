from data.users import create_user, get_user_by_username


def register_user(username, password, role="user"):

    # Check duplicate username
    existing = get_user_by_username(username)
    if existing:
        return {
            "success": False,
            "message": "Username already exists"
        }

    # Create user with password
    user = create_user(username, password, role)

    if not user:
        return {
            "success": False,
            "message": "Registration failed"
        }

    return {
        "success": True,
        "message": "User registered successfully"
    }
