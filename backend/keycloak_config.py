from fastapi_keycloak import Keycloak

keycloak = Keycloak(
    server_url="https://your-keycloak-server.com/auth",
    client_id="your-client-id",
    client_secret="your-client-secret",
    realm="your-realm-name",
    admin_user="your-admin-username",
    admin_password="your-admin-password",
)