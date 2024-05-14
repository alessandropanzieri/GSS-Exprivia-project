import Keycloak from "keycloak-js";

const keycloak = new Keycloak({
    realm: "GSS",
    clientId: "GSS",
    url: import.meta.env.KEYCLOAK_SERVER_URL
});

export default keycloak;