from pydantic import BaseModel

class EventBase(BaseModel):
    id: int