# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from crud import create_employee, get_all_employees, get_employee, update_employee, delete_employee
from database import employees_collection, administrative_collection, event_collection

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

# Astro frontend endpoint
@app.get("/astro-frontend")
async def astro_frontend():
    # Replace 'YOUR_FRONTEND_ENDPOINT' with the actual endpoint provided by your colleague
    frontend_endpoint = 'YOUR_FRONTEND_ENDPOINT'
    return {"astro_frontend_endpoint": frontend_endpoint}

# Your CRUD endpoints go here
# Example: Create employee
@app.post("/employees", response_model=dict)
async def create_employee_endpoint(employee: dict):
    return await create_employee(employee)

# Example: Get all employees
@app.get("/employees", response_model=list)
async def get_all_employees_endpoint(skip: int = 0, limit: int = 10):
    return await get_all_employees(skip, limit)

# Example: Get a single employee by ID
@app.get("/employees/{employee_id}", response_model=dict)
async def get_employee_endpoint(employee_id: str):
    return await get_employee(employee_id)

# Example: Update employee by ID
@app.put("/employees/{employee_id}", response_model=dict)
async def update_employee_endpoint(employee_id: str, updates: dict):
    return await update_employee(employee_id, updates)

# Example: Delete employee by ID
@app.delete("/employees/{employee_id}", response_model=dict)
async def delete_employee_endpoint(employee_id: str):
    return await delete_employee(employee_id)

