# keycloak/Dockerfile
FROM quay.io/keycloak/keycloak:23.0.1 as builder

# Enable health and metrics support
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true

# Configure the database vendor
ENV KC_DB=postgres

# Build and start Keycloak
RUN /opt/keycloak/bin/kc.sh build

FROM quay.io/keycloak/keycloak:23.0.1
COPY --from=builder /opt/keycloak/ /opt/keycloak/

# Copy custom realm configuration
COPY keycloak-config.json /opt/keycloak/data/import/realm-config.json

# Start Keycloak in production mode
ENTRYPOINT ["/opt/keycloak/bin/kc.sh", "start-dev", "--import-realm"]
