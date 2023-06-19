# keycloak_client.py - файл клиента для подключения  к  keyсloak для получения token
import requests

from config import (KEYCLOAK_ADMIN_CLIENT, KEYCLOAK_ADMIN_SECRET,
                    KEYCLOAK_GRANT_TYPE_CREDENTIALS,
                    KEYCLOAK_GRANT_TYPE_PASSWORD, KEYCLOAK_URL,
                    KEYCLOAK_USER_CLIENT, KEYCLOAK_USER_SECRET)
from decorators.decorator_log_http_request import log_http_request


class KeyCloakClient:
    def __init__(self):
        self.headers = {"Authorization": f'Bearer {self._admin_auth().get("access_token")}'}

    def _admin_auth(self, path='/realms/Exolve/protocol/openid-connect/token'):
        response = requests.post(
            url=f'{KEYCLOAK_URL}{path}',
            data={
                'client_secret': KEYCLOAK_ADMIN_SECRET,
                'grant_type': KEYCLOAK_GRANT_TYPE_CREDENTIALS,
                'client_id': KEYCLOAK_ADMIN_CLIENT
            },
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        response.raise_for_status()
        return response.json()

    @log_http_request
    def get_user_info(self, email, path='/admin/realms/Exolve/users'):
        response = requests.get(
            url=f'{KEYCLOAK_URL}{path}',
            params={
                'search': email
            },
            headers=self.headers
        )
        response.raise_for_status()
        return response

    @log_http_request
    def update_customer(self, user_id, customer_id=None, billing_number=None, path='/admin/realms/Exolve/users'):
        response = requests.put(
            url=f'{KEYCLOAK_URL}{path}/{user_id}',
            json={
                'attributes': {
                  "customer_id": customer_id,
                  "billing_number": billing_number
                },
                'emailVerified': True,
                'requiredActions': []
            },
            headers=self.headers
        )
        response.raise_for_status()
        return response

    @log_http_request
    def verified_email(self, user_id, path='/admin/realms/Exolve/users'):
        response = requests.put(
            url=f'{KEYCLOAK_URL}{path}/{user_id}',
            json={
                'emailVerified': True
            },
            headers=self.headers
        )
        response.raise_for_status()
        return response

    def auth_from_user(self, username, password, path='/realms/Exolve/protocol/openid-connect/token'):
        response = requests.post(
            url=f'{KEYCLOAK_URL}{path}',
            data={
                'client_id': KEYCLOAK_USER_CLIENT,
                'grant_type': KEYCLOAK_GRANT_TYPE_PASSWORD,
                'username': username,
                'password': password,
                'client_secret': KEYCLOAK_USER_SECRET
            },
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        response.raise_for_status()
        return response.json()

    def reset_password(self, user_id, password, path='/admin/realms/Exolve/users'):
        response = requests.put(
            url=f'{KEYCLOAK_URL}{path}/{user_id}/reset-password',
            json={
                "value": password
            },
            headers=self.headers
        )
        response.raise_for_status()
        return response

    @log_http_request
    def registration_customer(self, username, path='/admin/realms/Exolve/users'):
        response = requests.post(
            url=f'{KEYCLOAK_URL}{path}',
            json={
                'username': username,
                'enabled': True,
                'emailVerified': True,
                'email': username
            },
            headers=self.headers
        )
        response.raise_for_status()
        return response
