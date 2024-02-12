from typing import Optional
from pydantic import BaseModel

class EventSchema(BaseModel):
    id: Optional[str]

    date: str
    description: str
    employee_id: str