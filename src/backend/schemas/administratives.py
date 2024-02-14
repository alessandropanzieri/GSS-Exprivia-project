from typing import Optional
from pydantic import BaseModel

class AdministrativeSchema(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    birthdate: str
    email: str
    phone: str
    current_status: str