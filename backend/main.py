from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_keycloak import KeycloakUser

from routes import administrators, employees, events
from auth_dependencies import get_current_user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"]
)

app.include_router(administrators.router, prefix="/administrators", tags=["administrators"], dependencies=[Depends(get_current_user)])
app.include_router(employees.router, prefix="/employees", tags=["employees"], dependencies=[Depends(get_current_user(required_roles=["employee"]))])
app.include_router(events.router, prefix="/events", tags=["events"], dependencies=[Depends(get_current_user)])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)