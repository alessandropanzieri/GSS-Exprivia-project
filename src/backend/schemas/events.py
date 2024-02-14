from typing import Optional
from pydantic import BaseModel

class EventSchema(BaseModel):
    id: Optional[int]
    date: str
    description: str
    employee_id: int