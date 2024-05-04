import Keycloak from "keycloak-js";

const keycloak = new Keycloak({
    realm: "GSS",
    clientId: "GSS",
    url: "http://keycloak:8080/"
});

export default keycloak;