from fastapi import FastAPI
from routers import events, employees, administratives

app = FastAPI()

app.include_router(events.router, prefix = "/events", tags = ["events"])
app.include_router(employees.router, prefix = "/employees", tags = ["employees"])
app.include_router(administratives.router, prefix = "/administratives", tags = ["administratives"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)