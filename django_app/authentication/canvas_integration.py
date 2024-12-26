# django_app/authentication/canvas_integration.py
import requests

class CanvasLMSIntegration:
    def __init__(self, access_token):
        self.base_url = 'http://canvas:3000/api/v1'
        self.headers = {
            'Authorization': f'Bearer {access_token}'
        }

    def get_courses(self):
        response = requests.get(f'{self.base_url}/courses', headers=self.headers)
        return response.json()

    def create_course(self, name, course_code):
        payload = {
            'course': {
                'name': name,
                'course_code': course_code
            }
        }
        response = requests.post(f'{self.base_url}/accounts/1/courses', 
                                 json=payload, 
                                 headers=self.headers)
        return response.json()

# django_app/settings.py modifications
AUTHENTICATION_BACKENDS = [
    'authentication.keycloak_auth.KeycloakAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Additional Keycloak OIDC settings
KEYCLOAK_SERVER_URL = 'http://keycloak:8080/realms/django-canvas-realm'
KEYCLOAK_CLIENT_ID = 'django-client'
KEYCLOAK_CLIENT_SECRET = 'your-django-client-secret'