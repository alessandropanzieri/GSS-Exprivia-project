from bson import ObjectId
from ..database import get_database

def create_admin(admin: dict):
    administratives_collection = get_database().get_collection("administratives_collection")
    result = administratives_collection.insert_one(admin)
    created_admin = administratives_collection.find_one({"_id": result.inserted_id})
    return created_admin

def get_all_admins(skip: int = 0, limit: int = 10):
    administratives_collection = get_database().get_collection("administratives_collection")
    admin = administratives_collection.find().skip(skip).limit(limit).to_list(length=limit)
    return admin

def get_admin_by_id(admin_id: str):
    administratives_collection = get_database().get_collection("administratives_collection")
    existing_admin = administratives_collection.find_one({"_id": ObjectId(admin_id)})
    if existing_admin:
        return existing_admin
    return None

def update_admin(admin_id: str, updated_admin: dict):
    administratives_collection = get_database().get_collection("administratives_collection")
    result = administratives_collection.replace_one({"_id": ObjectId(admin_id)}, updated_admin)
    if result.modified_count:
        return administratives_collection.find_one({"_id": ObjectId(admin_id)})
    return None

def delete_admin(admin_id: str):
    administratives_collection = get_database().get_collection("administratives_collection")
    result = administratives_collection.delete_one({"_id": ObjectId(admin_id)})
    if result.deleted_count:
        return {"message": "admin deleted successfully"}
    return None