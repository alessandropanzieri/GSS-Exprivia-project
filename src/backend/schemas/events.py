from pydantic import BaseModel
from typing import Optional

class EventSchema(BaseModel):
    id: Optional[str]

    date: str
    description: str
    employee_id: str