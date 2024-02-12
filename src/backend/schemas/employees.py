from pydantic import BaseModel
from typing import Optional

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