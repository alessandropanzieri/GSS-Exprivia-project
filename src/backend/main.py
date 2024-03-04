from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import administrators, employees, events

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_headers = ["*"],
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["GET", "POST", "PUT", "DELETE"]
)

app.include_router(administrators.router, prefix = "/administrators", tags = ["administrators"])
app.include_router(employees.router, prefix = "/employees", tags = ["employees"])
app.include_router(events.router, prefix = "/events", tags = ["events"])