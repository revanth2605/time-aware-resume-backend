def can_view(requesting_user, target_user_id, visibility):
    if requesting_user["role"] == "admin":
        return True

    if requesting_user["user_id"] == target_user_id:
        return True

    return visibility == "public"
def is_admin(identity):
    return identity.get("role") == "admin"
