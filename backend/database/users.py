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

    return user["profile"]


def update_user_profile(user_id: str, new_data: dict):
    db = get_database()

    db.users.update_one(
        {"user_id": user_id},
        {"$set": {f"profile.{k}": v for k, v in new_data.items() if v is not None}},
        upsert=True
    )