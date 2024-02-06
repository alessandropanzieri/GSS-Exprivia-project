from bson import ObjectId
from fastapi import HTTPException
from pymongo.mongo_client import MongoClient

cluster = MongoClient("mongodb+srv://username:MrPssHYZc6X266Fc@cluster.ngvjtx4.mongodb.net/?retryWrites = true&w = majority")
database = cluster.DATABASE
events_collection = database.event_collection
employees_collection = database.employees_collection
administrative_collection = database.administrative_collection

def create_event(event: dict):
    try:
        result = events_collection.insert_one(event)
        created_event = events_collection.find_one({"_id": result.inserted_id})
        return created_event
    except Exception as e:
        print(f"Error creating event: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def get_all_events(skip: int = 0, limit: int = 10):
    try:
        events = events_collection.find().skip(skip).limit(limit).to_list(length = limit)
        return events
    except Exception as e:
        print(f"Error fetching events: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def get_event_by_id(event_id: str):
    try:
        existing_event = events_collection.find_one({"_id": ObjectId(event_id)})
        if existing_event:
            return existing_event
        raise HTTPException(status_code = 404, detail = f"Event with id {event_id} not found")
    except Exception as e:
        print(f"Error fetching event: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def update_event(event_id: str, updated_event: dict):
    try:
        result = events_collection.replace_one({"_id": ObjectId(event_id)}, updated_event)
        if result.modified_count:
            return events_collection.find_one({"_id": ObjectId(event_id)})
        raise HTTPException(status_code = 404, detail = f"Event with id {event_id} not found")
    except Exception as e:
        print(f"Error updating event: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def delete_event(event_id: str):
    try:
        result = events_collection.delete_one({"_id": ObjectId(event_id)})
        if result.deleted_count:
            return {"message": "Event deleted successfully"}
        raise HTTPException(status_code = 404, detail = f"Event with id {event_id} not found")
    except Exception as e:
        print(f"Error deleting event: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def create_employee(employee: dict):
    try:
        result = employees_collection.insert_one(employee)
        created_employee = employees_collection.find_one({"_id": result.inserted_id})
        return created_employee
    except Exception as e:
        print(f"Error creating employee: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def get_all_employees(skip: int = 0, limit: int = 10):
    try:
        employees = employees_collection.find().skip(skip).limit(limit).to_list(length = limit)
        return employees
    except Exception as e:
        print(f"Error fetching employees: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def get_employee_by_id(employee_id: str):
    try:
        existing_employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
        if existing_employee:
            return existing_employee
        raise HTTPException(status_code = 404, detail = f"Employee with id {employee_id} not found")
    except Exception as e:
        print(f"Error fetching employee: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def update_employee(employee_id: str, updated_employee: dict):
    try:
        result = employees_collection.replace_one({"_id": ObjectId(employee_id)}, updated_employee)
        if result.modified_count:
            return employees_collection.find_one({"_id": ObjectId(employee_id)})
        raise HTTPException(status_code = 404, detail = f"Employee with id {employee_id} not found")
    except Exception as e:
        print(f"Error updating employee: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def delete_employee(employee_id: str):
    try:
        result = employees_collection.delete_one({"_id": ObjectId(employee_id)})
        if result.deleted_count:
            return {"message": "Employee deleted successfully"}
        raise HTTPException(status_code = 404, detail = f"Employee with id {employee_id} not found")
    except Exception as e:
        print(f"Error deleting employee: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def create_administrative(administrative: dict):
    try:
        result = administrative_collection.insert_one(administrative)
        created_administrative = administrative_collection.find_one({"_id": result.inserted_id})
        return created_administrative
    except Exception as e:
        print(f"Error creating administrative employee: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def get_all_administrative(skip: int = 0, limit: int = 10):
    try:
        administrative_employees = administrative_collection.find().skip(skip).limit(limit).to_list(length = limit)
        return administrative_employees
    except Exception as e:
        print(f"Error fetching administrative employees: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def get_administrative_by_id(administrative_id: str):
    try:
        existing_administrative = administrative_collection.find_one({"_id": ObjectId(administrative_id)})
        if existing_administrative:
            return existing_administrative
        raise HTTPException(status_code = 404, detail = f"Administrative employee with id {administrative_id} not found")
    except Exception as e:
        print(f"Error fetching administrative employee: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def update_administrative(administrative_id: str, updated_administrative: dict):
    try:
        result = administrative_collection.replace_one({"_id": ObjectId(administrative_id)}, updated_administrative)
        if result.modified_count:
            return administrative_collection.find_one({"_id": ObjectId(administrative_id)})
        raise HTTPException(status_code = 404, detail = f"Administrative employee with id {administrative_id} not found")
    except Exception as e:
        print(f"Error updating administrative employee: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")

def delete_administrative(administrative_id: str):
    try:
        result = administrative_collection.delete_one({"_id": ObjectId(administrative_id)})
        if result.deleted_count:
            return {"message": "Administrative employee deleted successfully"}
        raise HTTPException(status_code = 404, detail = f"Administrative employee with id {administrative_id} not found")
    except Exception as e:
        print(f"Error deleting administrative employee: {str(e)}")
        raise HTTPException(status_code = 500, detail = "Internal Server Error")