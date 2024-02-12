from bson import ObjectId
from ..database import get_database

def create_employee(employee: dict):
    employees_collection = get_database().get_collection("employees_collection")
    result = employees_collection.insert_one(employee)
    created_employee = employees_collection.find_one({"_id": result.inserted_id})
    return created_employee

def get_all_employees(skip: int = 0, limit: int = 10):
    employees_collection = get_database().get_collection("employees_collection")
    employees = employees_collection.find().skip(skip).limit(limit).to_list(length=limit)
    return employees

def get_employee_by_id(employee_id: str):
    employees_collection = get_database().get_collection("employees_collection")
    existing_employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
    if existing_employee:
        return existing_employee
    return None

def update_employee(employee_id: str, updated_employee: dict):
    employees_collection = get_database().get_collection("employees_collection")
    result = employees_collection.replace_one({"_id": ObjectId(employee_id)}, updated_employee)
    if result.modified_count:
        return employees_collection.find_one({"_id": ObjectId(employee_id)})
    return None

def delete_employee(employee_id: str):
    employees_collection = get_database().get_collection("employees_collection")
    result = employees_collection.delete_one({"_id": ObjectId(employee_id)})
    if result.deleted_count:
        return {"message": "Employee deleted successfully"}
    return None