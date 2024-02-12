from fastapi import FastAPI
from routers import events

app = FastAPI()

app.include_router(events.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)