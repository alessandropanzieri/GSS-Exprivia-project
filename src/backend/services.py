from main import app
from typing import List
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from crud import (
    create_event,
    update_event,
    delete_event,
    get_all_events,
    get_event_by_id,
    create_employee,
    update_employee,
    delete_employee,
    get_all_employees,
    get_employee_by_id,
    delete_administrative,
    create_administrative,
    update_administrative,
    get_all_administrative,
    get_administrative_by_id
)

class Event(BaseModel):
    name: str
    description: str

class Employee(BaseModel):
    name: str
    role: str

class Administrative(BaseModel):
    name: str
    department: str

@app.post("/events/", response_model = dict)
def create_event_api(event: Event):
    created_event = create_event(jsonable_encoder(event))
    return created_event

@app.get("/events/", response_model = List[dict])
def get_all_events_api(skip: int = 0, limit: int = 10):
    events = get_all_events(skip = skip, limit = limit)
    return events

@app.get("/events/{event_id}", response_model = dict)
def get_event_by_id_api(event_id: str):
    event = get_event_by_id(event_id)
    if event:
        return event
    raise HTTPException(status_code = 404, detail = f"Event with id {event_id} not found")

@app.put("/events/{event_id}", response_model = dict)
def update_event_api(event_id: str, updated_event: Event):
    event = update_event(event_id, jsonable_encoder(updated_event))
    if event:
        return event
    raise HTTPException(status_code = 404, detail = f"Event with id {event_id} not found")

@app.delete("/events/{event_id}", response_model = dict)
def delete_event_api(event_id: str):
    result = delete_event(event_id)
    return result

@app.post("/employees/", response_model = dict)
def create_employee_api(employee: Employee):
    created_employee = create_employee(jsonable_encoder(employee))
    return created_employee

@app.get("/employees/", response_model = List[dict])
def get_all_employees_api(skip: int = 0, limit: int = 10):
    employees = get_all_employees(skip = skip, limit = limit)
    return employees

@app.get("/employees/{employee_id}", response_model = dict)
def get_employee_by_id_api(employee_id: str):
    employee = get_employee_by_id(employee_id)
    if employee:
        return employee
    raise HTTPException(status_code = 404, detail = f"Employee with id {employee_id} not found")

@app.put("/employees/{employee_id}", response_model = dict)
def update_employee_api(employee_id: str, updated_employee: Employee):
    employee = update_employee(employee_id, jsonable_encoder(updated_employee))
    if employee:
        return employee
    raise HTTPException(status_code = 404, detail = f"Employee with id {employee_id} not found")

@app.delete("/employees/{employee_id}", response_model = dict)
def delete_employee_api(employee_id: str):
    result = delete_employee(employee_id)
    return result

@app.post("/administrative/", response_model = dict)
def create_administrative_api(administrative: Administrative):
    created_administrative = create_administrative(jsonable_encoder(administrative))
    return created_administrative

@app.get("/administrative/", response_model = List[dict])
def get_all_administrative_api(skip: int = 0, limit: int = 10):
    administrative_employees = get_all_administrative(skip = skip, limit = limit)
    return administrative_employees

@app.get("/administrative/{administrative_id}", response_model = dict)
def get_administrative_by_id_api(administrative_id: str):
    administrative = get_administrative_by_id(administrative_id)
    if administrative:
        return administrative
    raise HTTPException(status_code = 404, detail = f"Administrative employee with id {administrative_id} not found")

@app.put("/administrative/{administrative_id}", response_model = dict)
def update_administrative_api(administrative_id: str, updated_administrative: Administrative):
    administrative = update_administrative(administrative_id, jsonable_encoder(updated_administrative))
    if administrative:
        return administrative
    raise HTTPException(status_code = 404, detail = f"Administrative employee with id {administrative_id} not found")

@app.delete("/administrative/{administrative_id}", response_model = dict)
def delete_administrative_api(administrative_id: str):
    result = delete_administrative(administrative_id)
    return result