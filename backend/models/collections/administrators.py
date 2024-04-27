from ..database import get_database

def create_administrator(administrator: dict):
    administrators_collection = get_database().get_collection("administrators")
    result = administrators_collection.insert_one(administrator)
    return administrators_collection.find_one({"_id": result.inserted_id})

def get_all_administrators(skip: int, limit: int):
    administrators_collection = get_database().get_collection("administrators")
    return [administrator for administrator in administrators_collection.find().skip(skip).limit(limit)]

def get_administrator_by_id(administrator_id: int):
    administrators_collection = get_database().get_collection("administrators")
    try:
        return administrators_collection.find_one({"id": administrator_id})
    except:
        return None

def update_administrator(administrator_id: int, updated_administrator: dict):
    administrators_collection = get_database().get_collection("administrators")
    administrators_collection.replace_one({"id": administrator_id}, updated_administrator)
    return administrators_collection.find_one({"id": administrator_id})

def delete_administrator(administrator_id: str):
    administrators_collection = get_database().get_collection("administrators")
    administrators_collection.delete_one({"id": administrator_id})
    return {"message": "administrator deleted successfully"}