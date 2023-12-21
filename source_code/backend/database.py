# database.py


from pymongo import MongoClient
from bson import ObjectId
from enum import Enum  # Import Enum
from fastapi import HTTPException  # Import HTTPException
from pydantic import BaseModel
from typing import Optional, List

# MongoDB connection
MONGODB_CONNECTION_STRING = "mongodb://localhost:27017/"
client = MongoClient(MONGODB_CONNECTION_STRING)
db = client["employees_db"]
employees_collection = db["employees"]

class Status(str, Enum):
    IN_SERVICE = 'in_service'
    RESIGNED = 'resigned'
    FIRED = 'fired'
    RETIRED = 'retired'

class Employee(BaseModel):
    id: Optional[str]
    personal_info: dict
    photo: str
    contacts: dict
    qualification: str
    current_assignment: str
    current_status: Status
    service_statuses: List[dict]

    class Config:
        arbitrary_types_allowed = True

# Additional CRUD operations for the database
def update_employee(employee_id: str, new_info: Employee):
    result = employees_collection.update_one(
        {"_id": ObjectId(employee_id)},
        {"$set": new_info.dict(exclude={"id"})}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail=f"Employee with {employee_id} does not exist")
    return get_employee(employee_id)

def get_employee(employee_id: str):
    employee = employees_collection.find_one({"_id": ObjectId(employee_id)})
    if not employee:
        raise HTTPException(status_code=404, detail=f"Employee with {employee_id} does not exist")
    return employee
