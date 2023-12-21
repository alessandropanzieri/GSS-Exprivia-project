# main.py

from enum import Enum  # Add this import

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import Optional, List
from httpx import AsyncClient


app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust with the actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/employees")
def get_all_employees_list(skip: int = 0, limit: int = 10):
    employees = employees_collection.find().skip(skip).limit(limit)
    return {"employees": list(employees)}

@app.post("/employees/{employee_id}/update")
def update_employee_info(employee_id: str, new_info: Employee):
    updated_employee = update_employee(employee_id, new_info)
    return {"updated": updated_employee}

@app.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: str):
    employee = get_employee(employee_id)
    return {"employee": employee}

@app.get("/employees/search")
def search_employees_by_name(name: str):
    employees = employees_collection.find({"personal_info.name": {"$regex": f".*{name}.*", "$options": "i"}})
    return {"employees": list(employees)}

@app.post("/employees")
def add_employee(employee: Employee):
    result = employees_collection.insert_one(employee.dict())
    added_employee = get_employee(str(result.inserted_id))
    return {"added": added_employee}

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: str):
    result = employees_collection.delete_one({"_id": ObjectId(employee_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"Employee with {employee_id} does not exist")
    return {"deleted": employee_id}
