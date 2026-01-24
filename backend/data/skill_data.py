from data.db import skills_collection


def get_skill(user_id, skill_name):
    return skills_collection.find_one({
        "user_id": user_id,
        "skill_name": skill_name
    })


def create_skill(user_id, skill_name, visibility="private"):
    skill = {
        "user_id": user_id,
        "skill_name": skill_name,
        "current_score": 10,
        "max_cap": 85,
        "visibility": visibility,
        "last_practiced": None,
        "certificate_count": 0,
        "code_count": 0
    }
    skills_collection.insert_one(skill)
    return skill


def get_or_create_skill(user_id, skill_name, visibility="private"):
    skill = get_skill(user_id, skill_name)
    if not skill:
        skill = create_skill(user_id, skill_name, visibility)
    return skill


def update_skill(skill):
    skills_collection.update_one(
        {"_id": skill["_id"]},
        {"$set": skill}
    )


def get_skills_by_user(user_id):
    return list(skills_collection.find({"user_id": user_id}))


def get_public_skills(user_id):
    return list(skills_collection.find({
        "user_id": user_id,
        "visibility": "public"
    }))
