from typing import List
from bson import ObjectId
from fastapi import HTTPException
from pymongo.mongo_client import MongoClient

cluster = MongoClient("mongodb+srv://username:MrPssHYZc6X266Fc@cluster.ngvjtx4.mongodb.net/?retryWrites=true&w=majority")
database = cluster.DATABASE
event_collection = database.event_collection
employees_collection = database.employees_collection
administrative_collection = database.administrative_collection

print("Connected to MongoDB")

# Convert ObjectId to string in the response
def convert_object_id_to_str(item):
    item["_id"] = str(item["_id"])
    return item

def create_employee(employee: dict):
    try:
        result = employees_collection.insert_one(employee)
        created_employee = employees_collection.find_one({"_id": result.inserted_id})
        return convert_object_id_to_str(created_employee)
    except Exception as e:
        print(f"Error creating employee: {str(e)}")
        raise

def get_all_employees(skip: int = 0, limit: int = 10):
    try:
        employees = employees_collection.find().skip(skip).limit(limit).to_list(length=limit)
        return list(map(convert_object_id_to_str, employees))
    except Exception as e:
        print(f"Error fetching employees: {str(e)}")
        raise

def get_employee(employee_id: str):
    try:
        existing_employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
        if existing_employee:
            return convert_object_id_to_str(existing_employee)
        raise HTTPException(status_code=404, detail=f"Employee with id {employee_id} not found")
    except Exception as e:
        print(f"Error fetching employee: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

def update_employee(employee_id: str, updates: dict):
    try:
        employees_collection.update_one({"_id": ObjectId(employee_id)}, {"$set": updates})
        updated_employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
        if updated_employee:
            return convert_object_id_to_str(updated_employee)
        raise
    except Exception as e:
        print(f"Error updating employee: {str(e)}")
        raise

def delete_employee(employee_id: str):
    try:
        deleted_employee = employees_collection.find_one_and_delete({"_id": ObjectId(employee_id)})
        if deleted_employee:
            return convert_object_id_to_str(deleted_employee)
        raise
    except Exception as e:
        print(f"Error deleting employee: {str(e)}")
        raise
# Funzione per creare un dipendente amministrativo

def create_administrative(administrative: dict):
    try:
        result = administrative_collection.insert_one(administrative)
        created_administrative = administrative_collection.find_one({"_id": result.inserted_id})
        return convert_object_id_to_str(created_administrative)
    except Exception as e:
        print(f"Error creating administrative employee: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Funzione per ottenere tutti i dipendenti amministrativi
def get_all_administrative(skip: int = 0, limit: int = 10):
    try:
        administrative_employees = administrative_collection.find().skip(skip).limit(limit).to_list(length=limit)
        return list(map(convert_object_id_to_str, administrative_employees))
    except Exception as e:
        print(f"Error fetching administrative employees: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Funzione per ottenere un singolo dipendente amministrativo per ID
def get_administrative(administrative_id: str):
    try:
        existing_administrative = administrative_collection.find_one({"_id": ObjectId(administrative_id)})
        if existing_administrative:
            return convert_object_id_to_str(existing_administrative)
        raise HTTPException(status_code=404, detail=f"Administrative employee with id {administrative_id} not found")
    except Exception as e:
        print(f"Error fetching administrative employee: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Funzione per creare un evento
def create_event(event: dict):
    try:
        result = event_collection.insert_one(event)
        created_event = event_collection.find_one({"_id": result.inserted_id})
        return convert_object_id_to_str(created_event)
    except Exception as e:
        print(f"Error creating event: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Funzione per ottenere tutti gli eventi
def get_all_events(skip: int = 0, limit: int = 10):
    try:
        events = event_collection.find().skip(skip).limit(limit).to_list(length=limit)
        return list(map(convert_object_id_to_str, events))
    except Exception as e:
        print(f"Error fetching events: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Funzione per ottenere un singolo evento per ID
def get_event(event_id: str):
    try:
        existing_event = event_collection.find_one({"_id": ObjectId(event_id)})
        if existing_event:
            return convert_object_id_to_str(existing_event)
        raise HTTPException(status_code=404, detail=f"Event with id {event_id} not found")
    except Exception as e:
        print(f"Error fetching event: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
# Funzione per eliminare un dipendente amministrativo per ID
def delete_administrative(administrative_id: str):
    try:
        result = administrative_collection.delete_one({"_id": ObjectId(administrative_id)})
        if result.deleted_count:
            return {"message": "Administrative employee deleted successfully"}
        raise HTTPException(status_code=404, detail=f"Administrative employee with id {administrative_id} not found")
    except Exception as e:
        print(f"Error deleting administrative employee: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Funzione per eliminare un evento per ID
def delete_event(event_id: str):
    try:
        result = event_collection.delete_one({"_id": ObjectId(event_id)})
        if result.deleted_count:
            return {"message": "Event deleted successfully"}
        raise HTTPException(status_code=404, detail=f"Event with id {event_id} not found")
    except Exception as e:
        print(f"Error deleting event: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")