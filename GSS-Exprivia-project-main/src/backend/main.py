from fastapi import FastAPI, Depends
from fastapi_keycloak import FastAPIKeycloak
from fastapi.middleware.cors import CORSMiddleware
from routes import events, employees, administrators

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_headers = ["*"],
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["POST", "GET", "PUT", "DELETE"]
)

idp = FastAPIKeycloak(
    realm = "GSS",
    client_id = "GSS",
    server_url = "http://keycloak:8080/",
    callback_uri = "http://backend:8000/docs",
    client_secret = "5RPPSMwANsWE0fXTIyC5qXIfNKSu6P7f",
    admin_client_secret = "k53cbpQE7B2qRL1j9qoOSexHLHnOB6xE"
)
idp.add_swagger_config(app)

app.include_router(events.router, prefix = "/events", tags = ["events"], dependencies = [Depends(idp.get_current_user())])
app.include_router(employees.router, prefix = "/employees", tags = ["employees"], dependencies = [Depends(idp.get_current_user())])
app.include_router(administrators.router, prefix = "/administrators", tags = ["administrators"], dependencies = [Depends(idp.get_current_user())])