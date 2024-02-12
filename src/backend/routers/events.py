from typing import List
from fastapi import APIRouter
from schemas.events import EventBase
from models.collections.events import *

router = APIRouter()

@router.get("/", response_model = List[EventBase])
def get_events():
    return get_all_events()