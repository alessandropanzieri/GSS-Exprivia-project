from typing import Optional
from pydantic import BaseModel

class AdminSchema(BaseModel):
    id: Optional[str]

    phone: str
    email: str
    last_name: str
    birthdate: str
    first_name: str
    current_status: str