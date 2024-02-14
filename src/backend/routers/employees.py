from typing import List
from fastapi import APIRouter
from models.collections.employees import *
from schemas.employees import EmployeeSchema

router = APIRouter()

@router.post("/", response_model = EmployeeSchema)
def create(employee: EmployeeSchema):
    return create_employee(dict(employee))

@router.get("/", response_model = List[EmployeeSchema])
def get_all(skip: int = 0, limit: int = 10):
    return get_all_employees(skip, limit)

@router.get("/{employee_id}", response_model = EmployeeSchema)
def get_by_id(employee_id: str):
    return get_employee_by_id(employee_id)

@router.put("/{employee_id}", response_model = EmployeeSchema)
def update(employee_id: str, employee: EmployeeSchema):
    return update_employee(employee_id, dict(employee))

@router.delete("/{employee_id}")
def delete(employee_id: str):
    return delete_employee(employee_id)