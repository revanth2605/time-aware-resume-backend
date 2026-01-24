import datetime
from utils.constants import (
    MAX_SCORE,
    CERTIFICATE_CAP,
    CODE_CAP,
    CERTIFICATE_INCREMENT,
    CODE_INCREMENTS
)
from services.decay_engine import apply_decay


def add_certificate_score(skill):
    """
    Increase score based on certificate (slow growth).
    """
    if skill["certificate_count"] * CERTIFICATE_INCREMENT >= CERTIFICATE_CAP:
        return skill

    skill["current_score"] += CERTIFICATE_INCREMENT
    return skill


def add_code_score(skill):
    """
    Increase score based on code submissions (diminishing returns).
    """
    count = skill["code_count"]

    if count < len(CODE_INCREMENTS):
        increment = CODE_INCREMENTS[count]
    else:
        increment = 0.1

    if skill["current_score"] + increment > MAX_SCORE:
        skill["current_score"] = MAX_SCORE
    else:
        skill["current_score"] += increment

    return skill


def finalize_score(skill):
    """
    Apply decay and cap score.
    """
    skill = apply_decay(skill)

    skill["current_score"] = min(skill["current_score"], MAX_SCORE)
    skill["last_practiced"] = datetime.datetime.now().isoformat()

    return skill
