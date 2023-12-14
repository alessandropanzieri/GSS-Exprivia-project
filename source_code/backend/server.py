from fastapi import FastAPI

server = FastAPI()

@server.get("/")
def index():

    return {"message": "Hello from FastAPI!"}
