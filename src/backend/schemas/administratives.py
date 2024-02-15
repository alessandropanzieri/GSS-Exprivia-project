from typing import Optional
from pydantic import BaseModel

class AdministrativeSchema(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    birthdate: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    current_status: Optional[str]