from bson import ObjectId
from ..database import get_database

def create_event(event: dict):
    events_collection = get_database().get_collection("events_collection")
    result = events_collection.insert_one(event)
    created_event = events_collection.find_one({"_id": result.inserted_id})
    return created_event

def get_all_events(skip: int = 0, limit: int = 10):
    events_collection = get_database().get_collection("events_collection")
    events = events_collection.find().skip(skip).limit(limit).to_list(length = limit)
    return events

def get_event_by_id(event_id: str):
    events_collection = get_database().get_collection("events_collection")
    existing_event = events_collection.find_one({"_id": ObjectId(event_id)})
    if existing_event:
        return existing_event
    return None

def update_event(event_id: str, updated_event: dict):
    events_collection = get_database().get_collection("events_collection")
    result = events_collection.replace_one({"_id": ObjectId(event_id)}, updated_event)
    if result.modified_count:
        return events_collection.find_one({"_id": ObjectId(event_id)})
    return None

def delete_event(event_id: str):
    events_collection = get_database().get_collection("events_collection")
    result = events_collection.delete_one({"_id": ObjectId(event_id)})
    if result.deleted_count:
        return {"message": "Event deleted successfully"}
    return None