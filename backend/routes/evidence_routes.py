from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId

from data.code_evidence import get_code_evidence_by_skill
from data.certificate_evidence import get_certificate_evidence_by_skill
from data.db import code_evidence_collection, certificate_evidence_collection

from data.skill_data import get_skill, update_skill
from services.skill_scoring import finalize_score

from utils.serializers import serialize_mongo_doc

evidence_bp = Blueprint("evidence", __name__)

# -----------------------------------
# CODE HISTORY
# -----------------------------------

@evidence_bp.route("/evidence/code/<skill_name>", methods=["GET"])
@jwt_required()
def get_code_history(skill_name):

    user_id = get_jwt_identity()

    records = get_code_evidence_by_skill(user_id, skill_name)

    return {
        "records": [serialize_mongo_doc(r) for r in records]
    }


# -----------------------------------
# CERTIFICATE HISTORY
# -----------------------------------

@evidence_bp.route("/evidence/certificate/<skill_name>", methods=["GET"])
@jwt_required()
def get_certificate_history(skill_name):

    user_id = get_jwt_identity()

    records = get_certificate_evidence_by_skill(user_id, skill_name)

    return {
        "records": [serialize_mongo_doc(r) for r in records]
    }


# -----------------------------------
# DELETE CODE EVIDENCE
# -----------------------------------

@evidence_bp.route("/evidence/code/<evidence_id>", methods=["DELETE"])
@jwt_required()
def delete_code_evidence(evidence_id):

    user_id = get_jwt_identity()

    evidence = code_evidence_collection.find_one({
        "_id": ObjectId(evidence_id),
        "user_id": user_id
    })

    if not evidence:
        return {"error": "Record not found"}, 404

    # Delete evidence
    code_evidence_collection.delete_one({"_id": ObjectId(evidence_id)})

    # Reduce skill count
    skill = get_skill(user_id, evidence["skill_name"])

    if skill and skill.get("code_count", 0) > 0:
        skill["code_count"] -= 1
        skill = finalize_score(skill)
        update_skill(skill)

    return {"message": "Code evidence deleted"}


# -----------------------------------
# DELETE CERTIFICATE EVIDENCE
# -----------------------------------

@evidence_bp.route("/evidence/certificate/<evidence_id>", methods=["DELETE"])
@jwt_required()
def delete_certificate_evidence(evidence_id):

    user_id = get_jwt_identity()

    evidence = certificate_evidence_collection.find_one({
        "_id": ObjectId(evidence_id),
        "user_id": user_id
    })

    if not evidence:
        return {"error": "Record not found"}, 404

    # Delete evidence
    certificate_evidence_collection.delete_one({"_id": ObjectId(evidence_id)})

    # Reduce skill count
    skill = get_skill(user_id, evidence["skill_name"])

    if skill and skill.get("certificate_count", 0) > 0:
        skill["certificate_count"] -= 1
        skill = finalize_score(skill)
        update_skill(skill)

    return {"message": "Certificate evidence deleted"}
