# django_app/authentication/keycloak_auth.py
from django.contrib.auth.backends import BaseBackend
from keycloak import KeycloakOpenID
from django.contrib.auth.models import User

class KeycloakAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        keycloak_client = KeycloakOpenID(
            server_url='http://keycloak:8080/realms/django-canvas-realm',
            client_id='django-client',
            client_secret='your-django-client-secret',
            realm_name='django-canvas-realm'
        )
        
        try:
            # Verify credentials with Keycloak
            token = keycloak_client.token(username, password)
            
            # Extract user info
            userinfo = keycloak_client.userinfo(token['access_token'])
            
            # Create or get Django user
            user, created = User.objects.get_or_create(
                username=userinfo['preferred_username'],
                email=userinfo['email']
            )
            return user
        except Exception as e:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None