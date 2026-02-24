from backend.database.mongo import get_database


def get_user_profile(user_id: str):
    db = get_database()

    user = db.users.find_one({"user_id": user_id})

    if not user:
        db.users.insert_one({
            "user_id": user_id,
            "profile": {}
        })
        return {}

    # return only values (for eligibility engine)
    profile = {}
    for k, v in user.get("profile", {}).items():
        profile[k] = v["value"]

    return profile


def update_user_profile(user_id: str, new_data: dict, source: str):
    db = get_database()

    user = db.users.find_one({"user_id": user_id})

    if not user:
        db.users.insert_one({
            "user_id": user_id,
            "profile": {}
        })
        user = db.users.find_one({"user_id": user_id})

    profile = user.get("profile", {})

    for key, value in new_data.items():
        if value is None:
            continue

        profile[key] = {
            "value": value,
            "source": source
        }

    db.users.update_one(
        {"user_id": user_id},
        {"$set": {"profile": profile}}
    )
def is_valid_name(name: str):

    if not name:
        return False

    bad_keywords = [
        "GUARDIAN",
        "FATHER",
        "MOTHER",
        "NAME",
        "ADDRESS",
        "SIGNATURE"
    ]

    name_upper = name.upper()

    for word in bad_keywords:
        if word in name_upper:
            return False

    # reject very short noisy OCR
    if len(name.split()) < 2:
        return False

    return True
