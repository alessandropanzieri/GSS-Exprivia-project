from ..database import get_database

administratives_collection = get_database().get_collection("administratives_collection")

def get_all_administratives():
    return []