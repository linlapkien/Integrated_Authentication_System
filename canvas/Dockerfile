# canvas/Dockerfile
FROM instructure/canvas-lms:latest

# Copy custom configuration
COPY canvas-config.yml /opt/canvas/config/canvas.yml

# Additional setup for Keycloak integration
RUN pip install python-jose

# Expose Canvas port
EXPOSE 3000

