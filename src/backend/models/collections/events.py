from ..database import get_database

events_collection = get_database().get_collection("events_collection")

def get_all_events():
    return []