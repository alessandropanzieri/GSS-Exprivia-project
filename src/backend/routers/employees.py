from fastapi import APIRouter
from typing import List, Union
from models.collections.employees import *
from schemas.employees import EmployeeSchema

router = APIRouter()

@router.post("/", response_model = EmployeeSchema)
def create(employee: EmployeeSchema):
    return create_employee(dict(employee))

@router.get("/", response_model = List[EmployeeSchema])
def get_all(skip: int = 0, limit: int = 10):
    return get_all_employees(skip, limit)

@router.get("/{employee_id}", response_model = Union[EmployeeSchema, None])
def get_by_id(employee_id: int):
    return get_employee_by_id(employee_id)

@router.put("/{employee_id}", response_model = EmployeeSchema)
def update(employee_id: int, updated_employee: EmployeeSchema):
    return update_employee(employee_id, dict(updated_employee))

@router.delete("/{employee_id}")
def delete(employee_id: int):
    return delete_employee(employee_id)