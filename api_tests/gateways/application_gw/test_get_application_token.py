import pytest
# import testit
from hamcrest import assert_that, contains_string, is_not

from helpers.application_gw.app_base_helper import help_create_application
from helpers.application_gw.error_texts import (
    error_invalid_uuid_format, error_not_found,
    error_value_length_must_be_at_least_1)
from helpers.application_gw.schema_methods import \
    schema_response_get_application_token
from helpers.base_helpers import assert_json_schema


class Test200:
    @pytest.mark.Smoke
    @testit.workItemIds(40627)
    @testit.displayName('Получить токен приложения GetToken')
    @testit.externalId('Получить токен приложения GetToken ')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    @pytest.mark.usefixtures('delete_all_apps')
    def test_get_application_token(self, app_gw):
        application_uuid = help_create_application(app_gw=app_gw).get("application_uuid")
        with testit.step('Вызвать метод GetToken - получить токен приложения'):
            response = app_gw.get_token(json_data={"application_uuid": application_uuid}).json()
            application_token = response.get("application_tokens")[0].get("token")
        with testit.step('Проверить схему ответа метода'):
            assert_json_schema(response, schema_response_get_application_token)
        with testit.step('Проверить, что токен получен'):
            assert_that(
                actual_or_assertion=application_token,
                matcher=is_not(None))


class Test400:
    @pytest.mark.Regress
    @testit.workItemIds(40628)
    @testit.displayName('Валидация параметра application_uuid, метод GetToken')
    @testit.externalId('Валидация параметра application_uuid, метод GetToken ')
    @pytest.mark.parametrize("application_uuid, error_text", [
        ('b1953b47-a14e-4919-883c-7ba64253867b', error_not_found),
        ('b1953b47-a14e-4919-883c-7ba64253867b1', error_invalid_uuid_format),
        ('b1953b47-a14e-4919-883c-7ba64253867', error_invalid_uuid_format),
        ('\"\"', error_invalid_uuid_format),
        (None, error_value_length_must_be_at_least_1),
        (None, error_invalid_uuid_format)
    ])
    def test_validate_application_uuid(self, app_gw, application_uuid, error_text):
        with testit.step('Вызвать метод GetToken с невалидным application_uuid'):
            response = app_gw.get_token(json_data={"application_uuid": application_uuid}).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=contains_string(error_text)
            )

    @pytest.mark.Regress
    @testit.workItemIds(40629)
    @testit.displayName('Получить токен удаленного приложения')
    @testit.externalId('Получить токен удаленного приложения')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    def test_get_deleted_application_token(self, app_gw):
        application_uuid = help_create_application(app_gw=app_gw).get("application_uuid")
        with testit.step('Удалить приложение'):
            app_gw.terminate(json_data={"application_uuid": application_uuid})
        with testit.step('Вызвать метод GetToken с application_uuid удалённого приложения'):
            response = app_gw.get_token(json_data={"application_uuid": application_uuid}).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=contains_string(error_not_found)
            )

    @pytest.mark.Regress
    @testit.workItemIds(55104)
    @testit.displayName('Выполнить запрос GetToken без параметров')
    @testit.externalId('Выполнить запрос GetToken без параметров')
    def test_get_application_info_without_parametrs(self, app_gw):
        with testit.step('Вызвать метод GetToken без параметров'):
            response = app_gw.get_token(json_data={}).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=contains_string(error_invalid_uuid_format)
            )
            assert_that(
                actual_or_assertion=error_msg,
                matcher=contains_string(error_value_length_must_be_at_least_1)
            )
