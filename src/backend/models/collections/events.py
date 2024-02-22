from ..database import get_database

def create_event(event: dict):
    events_collection = get_database().get_collection("events")
    result = events_collection.insert_one(event)
    return events_collection.find_one({"_id": result.inserted_id})

def get_all_events(employee_id: int, skip: int):
    events_collection = get_database().get_collection("events")
    return [event for event in events_collection.find({"employee_id": employee_id}).skip(skip)]

def get_event_by_id(event_id: int):
    events_collection = get_database().get_collection("events")
    try:
        return events_collection.find_one({"id": event_id})
    except:
        return None

def update_event(event_id: int, updated_event: dict):
    events_collection = get_database().get_collection("events")
    events_collection.replace_one({"id": event_id}, updated_event)
    return events_collection.find_one({"id": event_id})

def delete_event(event_id: str):
    events_collection = get_database().get_collection("events")
    events_collection.delete_one({"id": event_id})
    return {"message": "Event deleted successfully"}