import datetime
from utils.constants import DECAY_PER_DAY


def apply_decay(skill):
    """
    Applies long-term decay to a skill.
    Decay starts ONLY after 6 months (180 days) of inactivity.
    """

    # If skill was never practiced, do nothing
    if not skill.get("last_practiced"):
        return skill

    last_practiced_date = datetime.datetime.fromisoformat(
        skill["last_practiced"]
    )
    current_date = datetime.datetime.now()

    days_inactive = (current_date - last_practiced_date).days

    # Grace period: 6 months (180 days)
    if days_inactive <= 180:
        return skill

    # Apply decay ONLY after grace period
    decay_days = days_inactive - 180
    decay_amount = decay_days * DECAY_PER_DAY

    skill["current_score"] = max(
        skill["current_score"] - decay_amount,
        0
    )

    return skill
