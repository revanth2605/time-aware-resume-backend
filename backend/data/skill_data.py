from data.db import skills_collection


# -----------------------------------
# GET SINGLE SKILL
# -----------------------------------

def get_skill(user_id, skill_name):
    return skills_collection.find_one({
        "user_id": user_id,
        "skill_name": skill_name
    })


# -----------------------------------
# CREATE SKILL
# -----------------------------------

def create_skill(user_id, skill_name, visibility="private"):
    skill = {
        "user_id": user_id,
        "skill_name": skill_name,
        "current_score": 10,
        "max_cap": 85,
        "visibility": visibility,          # public / private
        "last_practiced": None,
        "certificate_count": 0,
        "code_count": 0
    }

    skills_collection.insert_one(skill)
    return skill


# -----------------------------------
# GET OR CREATE
# -----------------------------------

def get_or_create_skill(user_id, skill_name, visibility="private"):
    skill = get_skill(user_id, skill_name)

    if not skill:
        skill = create_skill(user_id, skill_name, visibility)

    return skill


# -----------------------------------
# UPDATE SKILL DATA
# -----------------------------------

def update_skill(skill):
    skills_collection.update_one(
        {"_id": skill["_id"]},
        {"$set": skill}
    )


# -----------------------------------
# GET ALL USER SKILLS
# -----------------------------------

def get_skills_by_user(user_id):
    return list(skills_collection.find({"user_id": user_id}))


# -----------------------------------
# GET ONLY PUBLIC SKILLS
# -----------------------------------

def get_public_skills(user_id):
    return list(skills_collection.find({
        "user_id": user_id,
        "$or": [
            {"visibility": "public"},
            {"visibility": {"$exists": False}}
        ]
    }))



# -----------------------------------
# CHANGE VISIBILITY LATER (NEW)
# -----------------------------------

def update_skill_visibility(user_id, skill_name, visibility):
    skills_collection.update_one(
        {
            "user_id": user_id,
            "skill_name": skill_name
        },
        {
            "$set": {"visibility": visibility}
        }
    )
