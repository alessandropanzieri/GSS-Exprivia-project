from ..database import get_database

employees_collection = get_database().get_collection("employees_collection")

def get_all_employees():
    return []