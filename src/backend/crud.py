# crud.py
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List
from fastapi import HTTPException

# MongoDB connection
try:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["cluster.gss_db"]
    employees_collection = db["employees"]
    administrative_collection = db["administrative_collection"]
    event_collection = db["event_collection"]
    print("Connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB: {str(e)}")

# Convert ObjectId to string in the response
def convert_object_id_to_str(item):
    item["_id"] = str(item["_id"])
    return item

# Create employee
async def create_employee(employee: dict):
    try:
        result = await employees_collection.insert_one(employee)
        created_employee = await employees_collection.find_one({"_id": result.inserted_id})
        return convert_object_id_to_str(created_employee)
    except Exception as e:
        print(f"Error creating employee: {str(e)}")
        raise

# Read all employees
async def get_all_employees(skip: int = 0, limit: int = 10):
    try:
        employees = await employees_collection.find().skip(skip).limit(limit).to_list(length=limit)
        return list(map(convert_object_id_to_str, employees))
    except Exception as e:
        print(f"Error fetching employees: {str(e)}")
        raise

# Read a single employee by ID
async def get_employee(employee_id: str):
    try:
        existing_employee = await employees_collection.find_one({"_id": ObjectId(employee_id)})
        if existing_employee:
            return convert_object_id_to_str(existing_employee)
        raise
    except Exception as e:
        print(f"Error fetching employee: {str(e)}")
        raise

# Update employee by ID
async def update_employee(employee_id: str, updates: dict):
    try:
        await employees_collection.update_one({"_id": ObjectId(employee_id)}, {"$set": updates})
        updated_employee = await employees_collection.find_one({"_id": ObjectId(employee_id)})
        if updated_employee:
            return convert_object_id_to_str(updated_employee)
        raise
    except Exception as e:
        print(f"Error updating employee: {str(e)}")
        raise

# Delete employee by ID
async def delete_employee(employee_id: str):
    try:
        deleted_employee = await employees_collection.find_one_and_delete({"_id": ObjectId(employee_id)})
        if deleted_employee:
            return convert_object_id_to_str(deleted_employee)
        raise
    except Exception as e:
        print(f"Error deleting employee: {str(e)}")
        raise
