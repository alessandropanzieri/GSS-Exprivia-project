from fastapi import APIRouter
from schemas.events import EventBase
from models.collections.events import *

router = APIRouter()

@router.get("/", response_model = list[EventBase])
def read_events():
    return get_all_events()