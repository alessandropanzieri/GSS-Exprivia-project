import Keycloak from "keycloak-js";

const keycloak = new Keycloak({
    realm: "GSS",
    clientId: "GSS",
    url: "http://localhost:8080/auth"
});

export default keycloak;