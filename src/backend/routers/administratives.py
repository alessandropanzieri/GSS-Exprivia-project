from typing import List
from fastapi import APIRouter
from schemas.administratives import AdminSchema
from models.collections.administratives import *

router = APIRouter()

@router.post("/", response_model = AdminSchema)
def create(admin: AdminSchema):
    return create_admin(dict(admin))

@router.get("/", response_model = List[AdminSchema])
def get_all(skip: int = 0, limit: int = 10):
    return get_all_admins(skip, limit)

@router.get("/{admin_id}", response_model = AdminSchema)
def get_by_id(admin_id: str):
    return get_admin_by_id(admin_id)

@router.put("/{admin_id}", response_model = AdminSchema)
def update(admin_id: str, admin: AdminSchema):
    return update_admin(admin_id, dict(admin))

@router.delete("/{admin_id}")
def delete(admin_id: str):
    return delete_admin(admin_id)