import datetime
from data.db import activities_collection


def log_activity(user_id, activity_type, visibility="private"):
    activity = {
        "user_id": user_id,
        "type": activity_type,
        "visibility": visibility,
        "created_at": datetime.datetime.now()
    }
    activities_collection.insert_one(activity)
    return activity


def get_user_activities(user_id):
    return list(activities_collection.find({"user_id": user_id}))


def get_public_activities(user_id):
    return list(activities_collection.find({
        "user_id": user_id,
        "visibility": "public"
    }))
