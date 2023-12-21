# frontend.py

from httpx import AsyncClient
from typing import Optional, List

class Employee:
    def __init__(self, id: str, personal_info: dict, photo: str, contacts: dict,
                 qualification: str, current_assignment: str, current_status: str,
                 service_statuses: List[dict]):
        self.id = id
        self.personal_info = personal_info
        self.photo = photo
        self.contacts = contacts
        self.qualification = qualification
        self.current_assignment = current_assignment
        self.current_status = current_status
        self.service_statuses = service_statuses

class DB:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get_all_employees(self, skip: int = 0, limit: int = 10) -> List[Employee]:
        async with AsyncClient() as client:
            response = await client.get(f"{self.base_url}/employees?skip={skip}&limit={limit}")
            employees = [Employee(**employee) for employee in response.json()["employees"]]
            return employees

    async def update_employee_info(self, employee_id: str, update_data: dict) -> Optional[Employee]:
        async with AsyncClient() as client:
            response = await client.post(f"{self.base_url}/employees/{employee_id}/update", json=update_data)
            updated_employee = response.json().get("updated")
            return Employee(**updated_employee) if updated_employee else None

    async def get_employee(self, employee_id: str) -> Optional[Employee]:
        async with AsyncClient() as client:
            response = await client.get(f"{self.base_url}/employees/{employee_id}")
            employee = response.json().get("employee")
            return Employee(**employee) if employee else None

    async def search_employees_by_name(self, name: str) -> List[Employee]:
        async with AsyncClient() as client:
            response = await client.get(f"{self.base_url}/employees/search?name={name}")
            employees = [Employee(**employee) for employee in response.json()["employees"]]
            return employees

    async def add_employee(self, employee_data: dict) -> Optional[Employee]:
        async with AsyncClient() as client:
            response = await client.post(f"{self.base_url}/employees", json=employee_data)
            added_employee = response.json().get("added")
            return Employee(**added_employee) if added_employee else None

    async def delete_employee(self, employee_id: str) -> Optional[str]:
        async with AsyncClient() as client:
            response = await client.delete(f"{self.base_url}/employees/{employee_id}")
            deleted_employee = response.json().get("deleted")
            return deleted_employee
