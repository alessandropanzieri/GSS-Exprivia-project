from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crud import create_employee, get_all_employees, get_employee, update_employee, delete_employee

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_origins = ["*"],
    allow_credentials = True,
)

@app.post("/employees", response_model = dict)
def create_employee_endpoint(employee: dict):
    return create_employee(employee)

@app.get("/employees", response_model = list)
def get_all_employees_endpoint(skip: int = 0, limit: int = 10):
    return get_all_employees(skip, limit)

@app.get("/employees/{employee_id}", response_model = dict)
def get_employee_endpoint(employee_id: str):
    return get_employee(employee_id)

@app.put("/employees/{employee_id}", response_model = dict)
def update_employee_endpoint(employee_id: str, updates: dict):
    return update_employee(employee_id, updates)

@app.delete("/employees/{employee_id}", response_model = dict)
def delete_employee_endpoint(employee_id: str):
    return delete_employee(employee_id)