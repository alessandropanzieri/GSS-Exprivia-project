from os import getenv
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from fastapi_keycloak import FastAPIKeycloak
from fastapi.middleware.cors import CORSMiddleware
from routes import events, employees, administrators

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_headers = ["*"],
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["POST", "GET", "PUT", "DELETE"]
)

idp = FastAPIKeycloak(
    realm = getenv("KEYCLOAK_REALM"),
    client_id = getenv("KEYCLOAK_CLIENT_ID"),
    server_url = getenv("KEYCLOAK_SERVER_URL"),
    callback_uri = getenv("KEYCLOAK_CALLBACK_URI"),
    client_secret = getenv("KEYCLOAK_CLIENT_SECRET"),
    admin_client_secret = getenv("KEYCLOAK_ADMIN_CLIENT_SECRET")
)
idp.add_swagger_config(app)

app.include_router(events.router, prefix = "/events", tags = ["events"], dependencies = [Depends(idp.get_current_user())])
app.include_router(employees.router, prefix = "/employees", tags = ["employees"], dependencies = [Depends(idp.get_current_user())])
app.include_router(administrators.router, prefix = "/administrators", tags = ["administrators"], dependencies = [Depends(idp.get_current_user())])