from ..database import get_database

def create_employee(employee: dict):
    employees_collection = get_database().get_collection("employees")
    result = employees_collection.insert_one(employee)
    return employees_collection.find_one({"_id": result.inserted_id})

def get_all_employees(skip: int, limit: int):
    employees_collection = get_database().get_collection("employees")
    return [employee for employee in employees_collection.find().skip(skip).limit(limit)]

def get_employee_by_id(employee_id: int):
    employees_collection = get_database().get_collection("employees")
    try:
        return employees_collection.find_one({"id": employee_id})
    except:
        return None

def update_employee(employee_id: int, updated_employee: dict):
    employees_collection = get_database().get_collection("employees")
    employees_collection.replace_one({"id": employee_id}, updated_employee)
    return employees_collection.find_one({"id": employee_id})

def delete_employee(employee_id: str):
    employees_collection = get_database().get_collection("employees")
    employees_collection.delete_one({"id": employee_id})
    return {"message": "employee deleted successfully"}