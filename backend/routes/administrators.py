from fastapi import APIRouter, Depends
from typing import List, Union
from models.collections.administrators import *
from schemas.administrators import AdministratorSchema
from fastapi_keycloak import Keycloak, KeycloakUser
from auth_dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=AdministratorSchema)
def create(administrators: AdministratorSchema, user: KeycloakUser = Depends(get_current_user)):
    return create_administrator(dict(administrators))

@router.get("/", response_model=List[AdministratorSchema])
def get_all(skip: int = 0, limit: int = 10, user: KeycloakUser = Depends(get_current_user)):
    return get_all_administrators(skip, limit)

@router.get("/{administrators_id}", response_model=Union[AdministratorSchema, None])
def get_by_id(administrators_id: int, user: KeycloakUser = Depends(get_current_user)):
    return get_administrator_by_id(administrators_id)

@router.put("/{administrators_id}", response_model=AdministratorSchema)
def update(administrators_id: int, updated_administrators: AdministratorSchema, user: KeycloakUser = Depends(get_current_user)):
    return update_administrator(administrators_id, dict(updated_administrators))

@router.delete("/{administrators_id}")
def delete(administrators_id: int, user: KeycloakUser = Depends(get_current_user)):
    return delete_administrator(administrators_id)