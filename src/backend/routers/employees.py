from typing import List
from fastapi import APIRouter
from models.collections.employees import *
from schemas.employees import EmployeeSchema

router = APIRouter()

@router.post("/", response_model = EmployeeSchema)
def create(employee: EmployeeSchema):
    created_employee = create_employee(employee.dict())
    if created_employee:
        return created_employee

@router.get("/", response_model = List[EmployeeSchema])
def get_all(skip: int = 0, limit: int = 10):
    return get_all_employees(skip, limit)

@router.get("/{employee_id}", response_model = EmployeeSchema)
def get_by_id(employee_id: str):
    employee = get_employee_by_id(employee_id)
    if employee:
        return employee

@router.put("/{employee_id}", response_model = EmployeeSchema)
def update(employee_id: str, employee: EmployeeSchema):
    updated_employee = update_employee(employee_id, employee.dict())
    if updated_employee:
        return updated_employee

@router.delete("/{employee_id}")
def delete(employee_id: str):
    result = delete_employee(employee_id)
    if result:
        return result