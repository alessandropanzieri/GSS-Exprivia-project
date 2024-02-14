from ..database import get_database

def create_administrative(administrative: dict):
    administratives_collection = get_database().get_collection("administratives_collection")
    result = administratives_collection.insert_one(administrative)
    return administratives_collection.find_one({"_id": result.inserted_id})

def get_all_administratives(skip: int, limit: int):
    administratives_collection = get_database().get_collection("administratives_collection")
    return [administrative for administrative in administratives_collection.find().skip(skip).limit(limit)]

def get_administrative_by_id(administrative_id: int):
    administratives_collection = get_database().get_collection("administratives_collection")
    try:
        return administratives_collection.find_one({"id": administrative_id})
    except:
        return None

def update_administrative(administrative_id: int, updated_administrative: dict):
    administratives_collection = get_database().get_collection("administratives_collection")
    administratives_collection.replace_one({"id": administrative_id}, updated_administrative)
    return administratives_collection.find_one({"id": administrative_id})

def delete_administrative(administrative_id: str):
    administratives_collection = get_database().get_collection("administratives_collection")
    administratives_collection.delete_one({"id": administrative_id})
    return {"message": "administrative deleted successfully"}