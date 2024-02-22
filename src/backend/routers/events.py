from fastapi import APIRouter
from typing import List, Union
from schemas.events import EventSchema
from models.collections.events import *

router = APIRouter()

@router.post("/", response_model = EventSchema)
def create(event: EventSchema):
    return create_event(dict(event))

@router.get("/{employee_id}", response_model = List[EventSchema])
def get_all(employee_id: int, skip: int = 0):
    return get_all_events(employee_id, skip)

@router.get("/{event_id}", response_model = Union[EventSchema, None])
def get_by_id(event_id: int):
    return get_event_by_id(event_id)

@router.put("/{event_id}", response_model = EventSchema)
def update(event_id: int, updated_event: EventSchema):
    return update_event(event_id, dict(updated_event))

@router.delete("/{event_id}")
def delete(event_id: int):
    return delete_event(event_id)