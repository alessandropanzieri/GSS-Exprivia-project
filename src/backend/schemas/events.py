from typing import Optional
from pydantic import BaseModel

class EventSchema(BaseModel):
    id: int
    date: Optional[str]
    description: Optional[str]
    employee_id: int