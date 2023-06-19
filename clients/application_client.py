# < service > _client.py - файл клиента методов тестируемого сервиса
# keycloak_client.py - файл клиента для подключения  к  keyсloak для получения token

import requests

from clients.keycloak_client import KeyCloakClient
from config import PUBLIC_GW_BASE_URL
from decorators.decorator_log_http_request import log_http_request
from decorators.decorator_log_http_request import smoke_check_requests


class APPGWClient(KeyCloakClient):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.token = KeyCloakClient.auth_from_user(self, username=username, password=password).get('access_token')
        self.headers = {"Authorization": f'Bearer {self.token}'}

    @log_http_request
    @smoke_check_requests
    def create(self, json_data,
               path="/application/v1/Create"):
        response = requests.post(url=f'{PUBLIC_GW_BASE_URL}{path}', json=json_data, headers=self.headers)
        return response

    @log_http_request
    @smoke_check_requests
    def get_info(self, json_data,
                 path="/application/v1/GetInfo"):
        response = requests.post(url=f'{PUBLIC_GW_BASE_URL}{path}', json=json_data, headers=self.headers)
        return response

    @log_http_request
    @smoke_check_requests
    def get_list(self, json_data,
                 path="/application/v1/GetList"):
        response = requests.post(url=f'{PUBLIC_GW_BASE_URL}{path}', json=json_data, headers=self.headers)
        return response

    @log_http_request
    @smoke_check_requests
    def get_token(self, json_data,
                  path="/application/v1/GetToken"):
        response = requests.post(url=f'{PUBLIC_GW_BASE_URL}{path}', json=json_data, headers=self.headers)
        return response

    @log_http_request
    @smoke_check_requests
    def update(self, json_data,
               path="/application/v1/Update"):
        response = requests.post(url=f'{PUBLIC_GW_BASE_URL}{path}', json=json_data, headers=self.headers)
        return response

    @log_http_request
    @smoke_check_requests
    def renew_token(self, json_data,
                    path="/application/v1/RenewToken"):
        response = requests.post(url=f'{PUBLIC_GW_BASE_URL}{path}', json=json_data, headers=self.headers)
        return response

    @log_http_request
    @smoke_check_requests
    def terminate(self, json_data,
                  path="/application/v1/Terminate"):
        response = requests.post(url=f'{PUBLIC_GW_BASE_URL}{path}', json=json_data, headers=self.headers)
        return response
