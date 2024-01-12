from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List, Optional

app = FastAPI()

# CORS middleware
origins = ["*"]  # Update this with your frontend's URL(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
try:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["GSSDatabase"]  # Update with your actual database name
    employees_collection = db["employees"]  # Update with your actual collection name
    print("Connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB: {str(e)}")

# Convert ObjectId to string in the response
def convert_object_id_to_str(item):
    item["_id"] = str(item["_id"])
    return item

# Create employee
@app.post("/employees", response_model=dict)
async def create_employee(employee: dict):
    try:
        result = await employees_collection.insert_one(employee)
        created_employee = await employees_collection.find_one({"_id": result.inserted_id})
        return convert_object_id_to_str(created_employee)
    except Exception as e:
        print(f"Error creating employee: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Read all employees
@app.get("/employees", response_model=List[dict])
async def get_all_employees(skip: int = 0, limit: int = 10):
    try:
        employees = await employees_collection.find().skip(skip).limit(limit).to_list(length=limit)
        return list(map(convert_object_id_to_str, employees))
    except Exception as e:
        print(f"Error fetching employees: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Read a single employee by ID
@app.get("/employees/{employee_id}", response_model=dict)
async def get_employee(employee_id: str):
    try:
        existing_employee = await employees_collection.find_one({"_id": ObjectId(employee_id)})
        if existing_employee:
            return convert_object_id_to_str(existing_employee)
        raise HTTPException(status_code=404, detail=f"Employee with id {employee_id} not found")
    except Exception as e:
        print(f"Error fetching employee: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Update employee by ID
@app.put("/employees/{employee_id}", response_model=dict)
async def update_employee(employee_id: str, updates: dict):
    try:
        await employees_collection.update_one({"_id": ObjectId(employee_id)}, {"$set": updates})
        updated_employee = await employees_collection.find_one({"_id": ObjectId(employee_id)})
        if updated_employee:
            return convert_object_id_to_str(updated_employee)
        raise HTTPException(status_code=404, detail=f"Employee with id {employee_id} not found")
    except Exception as e:
        print(f"Error updating employee: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Delete employee by ID
@app.delete("/employees/{employee_id}", response_model=dict)
async def delete_employee(employee_id: str):
    try:
        deleted_employee = await employees_collection.find_one_and_delete({"_id": ObjectId(employee_id)})
        if deleted_employee:
            return convert_object_id_to_str(deleted_employee)
        raise HTTPException(status_code=404, detail=f"Employee with id {employee_id} not found")
    except Exception as e:
        print(f"Error deleting employee: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
