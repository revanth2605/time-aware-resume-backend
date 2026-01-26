from data.db import code_evidence_collection
from datetime import datetime


def add_code_evidence(user_id, skill_name, metadata=None):
    evidence = {
        "user_id": user_id,
        "skill_name": skill_name,
        "type": "code",
        "metadata": metadata or {},
        "created_at": datetime.utcnow()
    }

    code_evidence_collection.insert_one(evidence)
    return evidence


def get_code_evidence_by_skill(user_id, skill_name):
    return list(
        code_evidence_collection.find({
            "user_id": user_id,
            "skill_name": skill_name
        }).sort("created_at", -1)
    )
