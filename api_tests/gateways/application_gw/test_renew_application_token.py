import pytest
import testit
# from hamcrest import assert_that, contains_string, equal_to, is_not

# from helpers.application_gw.app_base_helper import (help_create_application,
#                                                     help_get_application_token)
from helpers.application_gw.error_texts import (
    error_customer_status_blocked, error_invalid_uuid_format, error_not_found,
    error_value_length_must_be_at_least_1)
from helpers.application_gw.schema_methods import \
    schema_response_renew_application_token
# from helpers.base_helpers import assert_json_schema
# from helpers.cma.helper_functions import refresh_customer_state


class Test200:
    @pytest.mark.Smoke
    # @testit.workItemIds(39833)
    @testit.displayName('Обновить токен приложения пользователем с неподписанным контрактом')
    @testit.externalId('Обновить токен приложения пользователем с неподписанным контрактом')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_not_signed')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed_teardown')
    def test_renew_application_token_not_signed_customer(self, app_gw, cma, customer_gw):
        application_uuid = help_create_application(app_gw=app_gw).get("application_uuid")
        application_token = help_get_application_token(app_gw=app_gw, application_uuid=application_uuid)
        with testit.step('Вызвать метод RenewToken - пересоздать токен приложения'):
            response = app_gw.renew_token(json_data={"application_uuid": application_uuid}).json()
            application_recreated_token = response.get("application_token").get("token")
        with testit.step('Проверить схему ответа метода'):
            assert_json_schema(response, schema_response_renew_application_token)
        application_recreated_token_info = help_get_application_token(app_gw=app_gw,
                                                                      application_uuid=application_uuid)
        with testit.step('Убедиться, что при получении данных о приложении приходит пересозданный токен'):
            assert_that(
                actual_or_assertion=application_recreated_token,
                matcher=equal_to(application_recreated_token_info)
            )
        with testit.step('Убедиться, что токен приложения не совпадает с тем, что был при создании приложения'):
            assert_that(application_recreated_token, is_not(application_token))

    @pytest.mark.Smoke
    @testit.workItemIds(39833)
    @testit.displayName('Обновить токен приложения пользователем с подписанным контрактом')
    @testit.externalId('Обновить токен приложения пользователем с подписанным контрактом')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    @pytest.mark.usefixtures('delete_all_apps')
    def test_renew_application_token_signed_customer(self, app_gw, cma, customer_gw):
        application_uuid = help_create_application(app_gw=app_gw).get("application_uuid")
        application_token = help_get_application_token(app_gw=app_gw, application_uuid=application_uuid)
        with testit.step('Вызвать метод RenewToken - пересоздать токен приложения'):
            response = app_gw.renew_token(json_data={"application_uuid": application_uuid}).json()
            application_recreated_token = response.get("application_token").get("token")
        with testit.step('Проверить схему ответа метода'):
            assert_json_schema(response, schema_response_renew_application_token)
        application_recreated_token_info = help_get_application_token(app_gw=app_gw,
                                                                      application_uuid=application_uuid)
        with testit.step('Убедиться, что при получении данных о приложении приходит пересозданный токен'):
            assert_that(
                actual_or_assertion=application_recreated_token,
                matcher=equal_to(application_recreated_token_info)
            )
        with testit.step('Убедиться, что токен приложения не совпадает с тем, что был при создании приложения'):
            assert_that(application_recreated_token, is_not(application_token))


class Test400:
    @pytest.mark.Smoke
    @testit.workItemIds(54329)
    @testit.displayName('Обновить токен приложения пользователем в статусе {state}-{state_attributes}')
    @testit.externalId('Обновитьтокен приложения пользователем в статусе {state}-{state_attributes}')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed_teardown')
    @pytest.mark.usefixtures('delete_all_apps')
    @pytest.mark.parametrize("state, state_attributes", [
        ('CUSTOMER_STATE_BLOCKED', 'suspend'),
        ('CUSTOMER_STATE_BLOCKED', 'admin')
    ])
    def test_renew_application_token_customer_blocked(self, app_gw, cma, customer_gw, state, state_attributes):
        application_uuid = help_create_application(app_gw=app_gw).get('application_uuid')
        refresh_customer_state(cma=cma, customer_gw=customer_gw, state=state, state_attributes=state_attributes,
                               username=customer_gw.username)
        with testit.step('Вызвать метод RenewToken - пересоздать токен приложения'):
            response = app_gw.renew_token(json_data={"application_uuid": application_uuid}).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=equal_to(error_customer_status_blocked)
            )

    @pytest.mark.Regress
    @testit.workItemIds(39834)
    @testit.displayName('Пересоздать токен для удаленного приложения')
    @testit.externalId('Пересоздать токен для удаленного приложения')
    @pytest.mark.usefixtures("refresh_customer_state_to_active_signed")
    def test_recreate_token_for_terminated_application(self, app_gw):
        application_uuid = help_create_application(app_gw=app_gw).get("application_uuid")
        with testit.step('Удалить приложение'):
            app_gw.terminate(json_data={"application_uuid": application_uuid})
        with testit.step('Вызвать метод RenewToken с application_uuid удалённого приложения'):
            response = app_gw.renew_token(json_data={"application_uuid": application_uuid}).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=contains_string(error_not_found)
            )

    @pytest.mark.Regress
    @testit.workItemIds(40241)
    @testit.displayName('Валидация параметра application_uuid, метод RenewToken')
    @testit.externalId('Валидация параметра application_uuid, метод RenewToken ')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    @pytest.mark.parametrize("application_uuid, error_text", [
        ('b1953b47-a14e-4919-883c-7ba64253867b', error_not_found),
        ('b1953b47-a14e-4919-883c-7ba64253867b1', error_invalid_uuid_format),
        ('b1953b47-a14e-4919-883c-7ba64253867', error_invalid_uuid_format),
        ('\"\"', error_invalid_uuid_format),
        (None, error_value_length_must_be_at_least_1),
        (None, error_invalid_uuid_format)
    ])
    def test_validate_application_uuid(self, app_gw, application_uuid, error_text):
        with testit.step('Вызвать метод RenewToken с невалидным application_uuid'):
            response = app_gw.renew_token(json_data={"application_uuid": application_uuid}).json()
        with testit.step('Проверить сообщение об ошибке'):
            error_msg = response.get('error')
            assert_that(
                actual_or_assertion=error_msg,
                matcher=contains_string(error_text)
            )

    @pytest.mark.Regress
    @testit.workItemIds(55105)
    @testit.displayName('Выполнить запрос RenewToken без параметров')
    @testit.externalId('Выполнить запрос RenewToken без параметров')
    @pytest.mark.usefixtures('refresh_customer_state_to_active_signed')
    def test_get_application_info_without_parametrs(self, app_gw):
        with testit.step('Вызвать метод RenewToken без параметров'):
            response = app_gw.renew_token(json_data={}).json()
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
