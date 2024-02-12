from typing import List
from fastapi import APIRouter
from models.collections.administratives import *
from schemas.administratives import AdministrativeBase

router = APIRouter()

@router.get("/", response_model = List[AdministrativeBase])
def get_administratives():
    return get_all_administratives()