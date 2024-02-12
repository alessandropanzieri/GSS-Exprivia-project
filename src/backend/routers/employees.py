from typing import List
from fastapi import APIRouter
from schemas.employees import EmployeeBase
from models.collections.employees import *

router = APIRouter()

@router.get("/", response_model = list[EmployeeBase])
def get_employees():
    return get_all_employees()