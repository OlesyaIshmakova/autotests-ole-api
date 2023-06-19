# config.py - файл инициализации переменных из .env.<zone>

import pytest
import testit
from hamcrest import assert_that, contains_string, equal_to

from helpers.application_gw.error_texts import (
    error_create_application_already_exist,
    error_create_two_app_status_potential, error_customer_status_blocked,
    error_invalid_for_string, error_value_length_must_be_at_most_90,
    error_value_length_must_between_1_or_40)
from helpers.application_gw.schema_methods import (
    schema_response_create_application, schema_response_error)

# from helpers.base_helpers import assert_json_schema, get_body_error_msg
# from helpers.cma.helper_functions import refresh_customer_state
# from helpers.exceptions import StatusCode5XX
# from helpers.generate_data import generate_text


class Test200:
    @pytest.mark.Smoke
    @testit.workItemIds(38717)
    @testit.displayName('Создание нового приложения с неподписанным контрактом')
    @testit.externalId('Создание нового приложения с неподписанным контрактом')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_not_signed')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed_teardown')
    @pytest.mark.usefixtures('delete_all_apps')
    def test_create_application(self, app_gw):
        with testit.step('Вызвать метод Create - создать новое приложение с корректными параметрами'):
            body = {
                "application_name": generate_text(min_chars=10, max_chars=40),
                "application_description": generate_text(min_chars=10, max_chars=40)
            }
            response = app_gw.create(json_data=body).json()
        with testit.step('Проверить схему ответа метода'):
            assert_json_schema(response=response, schema=schema_response_create_application)

    @pytest.mark.Smoke
    @testit.workItemIds(54326)
    @testit.displayName('Создание двух приложений пользователем с подписанным контрактом')
    @testit.externalId('Создание двух приложений пользователем с подписанным контрактом')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    @pytest.mark.usefixtures('delete_all_apps')
    def test_create_two_applications_signed_customer(self, app_gw):
        with testit.step('Вызвать метод Create - создать новое приложение с корректными параметрами'):
            body = {
                "application_name": generate_text(min_chars=10, max_chars=40),
                "application_description": generate_text(min_chars=10, max_chars=40)
            }
            app_gw.create(json_data=body).json()
        with testit.step('Вызвать метод Create - создать второе приложение'):
            body = {
                "application_name": generate_text(min_chars=10, max_chars=40),
                "application_description": generate_text(min_chars=10, max_chars=40)
            }
            response = app_gw.create(json_data=body).json()
        with testit.step('Проверить схему ответа метода'):
            assert_json_schema(response=response, schema=schema_response_create_application)


class Test400:
    @pytest.mark.Regress
    @testit.workItemIds(40096)
    @pytest.mark.xfail(raises=StatusCode5XX)
    @testit.displayName('Создание дубликата приложения')
    @testit.externalId('Создание дубликата приложения')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    @pytest.mark.usefixtures('delete_all_apps')
    @testit.links('https://jira.mtt.ru:8443/browse/DPRNM-803')
    def test_create_application_with_used_name(self, app_gw):
        with testit.step('Вызвать метод Create - создать первое приложение'):
            body = {
                "application_name": generate_text(min_chars=10, max_chars=40),
                "application_description": generate_text(min_chars=10, max_chars=40)
            }
            response = app_gw.create(json_data=body).json()
            app_name_used = response.get('application_name')
        with testit.step('Вызвать метод Create'
                         ' - создать второе приложение с application_name первого приложения'):
            body = {
                "application_name": app_name_used,
                "application_description": generate_text(min_chars=10, max_chars=40)
            }
            response = app_gw.create(json_data=body).json()
            error_msg = response.get('error')
        with testit.step('Проверить схему ответа метода'):
            assert_json_schema(response, schema_response_error)
        with testit.step('Проверить вывод ошибки'):
            assert_that(
                actual_or_assertion=get_body_error_msg(msg=error_msg, param_name="ERROR"),
                matcher=equal_to([error_create_application_already_exist(application_name=app_name_used)])
            )

    @pytest.mark.Smoke
    @testit.workItemIds(54327)
    @testit.displayName('Создание двух приложений пользователем с неподписанным контрактом')
    @testit.externalId('Создание двух приложений пользователем с неподписанным контрактом')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_not_signed')
    @pytest.mark.usefixtures('delete_all_apps')
    def test_create_two_applications_not_signed_customer(self, app_gw):
        with testit.step('Вызвать метод CreateApplication - создать новое приложение с корректными параметрами'):
            body = {
                "application_name": generate_text(min_chars=10, max_chars=40),
                "application_description": generate_text(min_chars=10, max_chars=40)
            }
            app_gw.create(json_data=body).json()
        with testit.step('Вызвать метод Create - создать второе приложение'):
            body = {
                "application_name": generate_text(min_chars=10, max_chars=40),
                "application_description": generate_text(min_chars=10, max_chars=40)
            }
            response = app_gw.create(json_data=body).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=equal_to(error_create_two_app_status_potential)
            )

    @pytest.mark.Smoke
    @testit.workItemIds(54328)
    @testit.displayName('Создание приложения пользователем в статусе {state}-{state_attributes}')
    @testit.externalId('Создание приложения пользователем в статусе {state}-{state_attributes}')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed_teardown')
    @pytest.mark.usefixtures('delete_all_apps')
    @pytest.mark.parametrize("state, state_attributes", [
        ('CUSTOMER_STATE_BLOCKED', 'suspend'),
        ('CUSTOMER_STATE_BLOCKED', 'admin')
    ])
    def test_create_application_customer_blocked(self, cma, customer_gw, app_gw, state, state_attributes):
        refresh_customer_state(cma=cma, customer_gw=customer_gw, state=state, state_attributes=state_attributes,
                               username=customer_gw.username)
        with testit.step('Вызвать метод Create - создать новое приложение с корректными параметрами'):
            body = {
                "application_name": generate_text(min_chars=10, max_chars=40),
                "application_description": generate_text(min_chars=10, max_chars=40)
            }
            response = app_gw.create(json_data=body).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=equal_to(error_customer_status_blocked)
            )

    @pytest.mark.Regress
    @testit.workItemIds(40110)
    @testit.displayName('Создать приложение без параметров')
    @testit.externalId('Создать приложение без параметров')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    def test_create_application_without_parameters(self, app_gw):
        with testit.step('Вызвать метод CreateApplication без параметров'):
            response = app_gw.create(json_data={}).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=contains_string(error_value_length_must_between_1_or_40)
            )

    @pytest.mark.Regress
    @testit.workItemIds(39640)
    @testit.displayName('Валидация поля application_name в методе Create')
    @testit.externalId('Валидация поля application_name в методе Create')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    @pytest.mark.parametrize("application_name, error_text", [
        ("q"*41, error_value_length_must_between_1_or_40),
        ('', error_value_length_must_between_1_or_40),
        (None, error_value_length_must_between_1_or_40),
        (43, error_invalid_for_string(43))
    ])
    def test_validate_application_name(self, app_gw, application_name, error_text):
        with testit.step('Вызвать метод CreateApplication с невалидным application_name'):
            body = {
                "application_name": application_name
            }
            response = app_gw.create(json_data=body).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=contains_string(error_text)
            )

    @pytest.mark.Regress
    @testit.workItemIds(39641)
    @testit.displayName('Валидация поля application_description в методе Create')
    @testit.externalId('Валидация поля application_description в методе Create')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    def test_validate_application_description(self, app_gw):
        with testit.step('Вызвать метод CreateApplication с невалидным application_description'):
            body = {
                "application_name": generate_text(min_chars=10, max_chars=40),
                "application_description": generate_text(min_chars=91, max_chars=91)
            }
            response = app_gw.create(json_data=body).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=contains_string(error_value_length_must_be_at_most_90)
            )
