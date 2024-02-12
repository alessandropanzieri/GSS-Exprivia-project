from typing import List
from fastapi import APIRouter
from schemas.administratives import AdminSchema
from models.collections.administratives import *

router = APIRouter()

@router.post("/", response_model = AdminSchema)
def create(admin: AdminSchema):
    created_admin = create_admin(admin.dict())
    if created_admin:
        return created_admin

@router.get("/", response_model = List[AdminSchema])
def get_all(skip: int = 0, limit: int = 10):
    return get_all_admins(skip, limit)

@router.get("/{admin_id}", response_model = AdminSchema)
def get_by_id(admin_id: str):
    admin = get_admin_by_id(admin_id)
    if admin:
        return admin

@router.put("/{admin_id}", response_model = AdminSchema)
def update(admin_id: str, admin: AdminSchema):
    updated_admin = update_admin(admin_id, admin.dict())
    if updated_admin:
        return updated_admin

@router.delete("/{admin_id}")
def delete(admin_id: str):
    result = delete_admin(admin_id)
    if result:
        return result