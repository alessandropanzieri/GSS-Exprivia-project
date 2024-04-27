from fastapi import Depends, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from fastapi_keycloak import Keycloak, KeycloakUser

from keycloak_config import keycloak

async def get_current_user(
    keycloak_instance: Keycloak = Depends(keycloak),
    required_roles: list[str] = [],
) -> KeycloakUser:
    user = await keycloak_instance.get_current_user()

    if not user:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Not authenticated",
        )

    if required_roles and not any(role in user.roles for role in required_roles):
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Insufficient permissions",
        )

    return user