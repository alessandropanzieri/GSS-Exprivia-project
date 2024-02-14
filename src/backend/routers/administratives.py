from fastapi import APIRouter
from typing import List, Union
from models.collections.administratives import *
from schemas.administratives import AdministrativeSchema

router = APIRouter()

@router.post("/", response_model = AdministrativeSchema)
def create(administrative: AdministrativeSchema):
    return create_administrative(dict(administrative))

@router.get("/", response_model = List[AdministrativeSchema])
def get_all(skip: int = 0, limit: int = 10):
    return get_all_administratives(skip, limit)

@router.get("/{administrative_id}", response_model = Union[AdministrativeSchema, None])
def get_by_id(administrative_id: int):
    return get_administrative_by_id(administrative_id)

@router.put("/{administrative_id}", response_model = AdministrativeSchema)
def update(administrative_id: int, updated_administrative: AdministrativeSchema):
    return update_administrative(administrative_id, dict(updated_administrative))

@router.delete("/{administrative_id}")
def delete(administrative_id: int):
    return delete_administrative(administrative_id)