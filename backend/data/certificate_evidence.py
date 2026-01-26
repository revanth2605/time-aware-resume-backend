from data.db import certificate_evidence_collection
from datetime import datetime


def add_certificate_evidence(user_id, skill_name, metadata=None):
    evidence = {
        "user_id": user_id,
        "skill_name": skill_name,
        "type": "certificate",
        "metadata": metadata or {},
        "created_at": datetime.utcnow()
    }

    certificate_evidence_collection.insert_one(evidence)
    return evidence


def get_certificate_evidence_by_skill(user_id, skill_name):
    return list(
        certificate_evidence_collection.find({
            "user_id": user_id,
            "skill_name": skill_name
        }).sort("created_at", -1)
    )
