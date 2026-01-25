from services.skill_scoring import (
    add_certificate_score,
    add_code_score,
    finalize_score
)
from data.skill_data import update_skill


def process_certificate(skill):

    # Safety for older records
    if "certificate_count" not in skill:
        skill["certificate_count"] = 0

    skill["certificate_count"] += 1

    skill = add_certificate_score(skill)
    skill = finalize_score(skill)

    update_skill(skill)
    return skill


def process_code(skill):

    # Safety for older records
    if "code_count" not in skill:
        skill["code_count"] = 0

    skill["code_count"] += 1

    skill = add_code_score(skill)
    skill = finalize_score(skill)

    update_skill(skill)
    return skill
