from fastapi import FastAPI
from routers import administratives, employees, events

app = FastAPI()

app.include_router(administratives.router, prefix = "/administratives", tags = ["administratives"])
app.include_router(employees.router, prefix = "/employees", tags = ["employees"])
app.include_router(events.router, prefix = "/events", tags = ["events"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload = True)