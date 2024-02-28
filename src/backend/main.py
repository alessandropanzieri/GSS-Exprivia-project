from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import administratives, employees, events

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_headers = ["*"],
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["GET", "POST", "PUT", "DELETE"]
)

app.include_router(administratives.router, prefix = "/administratives", tags = ["administratives"])
app.include_router(employees.router, prefix = "/employees", tags = ["employees"])
app.include_router(events.router, prefix = "/events", tags = ["events"])