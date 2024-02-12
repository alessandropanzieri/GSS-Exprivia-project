from typing import Optional
from pydantic import BaseModel

class EmployeeSchema(BaseModel):
    id: Optional[str]

    rank: str
    phone: str
    email: str
    last_name: str
    birthdate: str
    first_name: str
    assignment: str
    current_status: str