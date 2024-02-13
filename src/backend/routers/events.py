from typing import List
from fastapi import APIRouter
from schemas.events import EventSchema
from models.collections.events import *

router = APIRouter()

@router.post("/", response_model = EventSchema)
def create_event(event: EventSchema):
    created_event = create_event(dict(event))
    if created_event:
        return created_event

@router.get("/", response_model = List[EventSchema])
def read_events(skip: int = 0, limit: int = 10):
    return get_all_events(skip, limit)

@router.get("/{event_id}", response_model = EventSchema)
def read_event(event_id: str):
    event = get_event_by_id(event_id)
    if event:
        return event

@router.put("/{event_id}", response_model = EventSchema)
def update_event(event_id: str, event: EventSchema):
    updated_event = update_event(event_id, event.dict())
    if updated_event:
        return updated_event

@router.delete("/{event_id}")
def delete_event(event_id: str):
    result = delete_event(event_id)
    if result:
        return result