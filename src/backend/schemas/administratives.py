from pydantic import BaseModel
from typing import Optional

class AdministrativeSchema(BaseModel):
    id: Optional[str]

    phone: str
    email: str
    last_name: str
    birthdate: str
    first_name: str
    current_status: str