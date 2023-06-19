import time

from grpc import StatusCode

from config import DELAY_SEC, DELAY_SEC_SHORT
from helpers.base_helpers import get_obj_list_from_objects_by_field_value
from helpers.customer_gw.cgw_base_helper import help_get_state
from helpers.customer_gw.enum_helper import customer_state_int
from helpers.messaging_gw.enum_helper import status_send_sms_int
from helpers.messaging_gw.ms_base_helper import \
    help_get_list as help_get_list_ms
from helpers.statistics_gw.statistics_base_helper import \
    help_get_list as help_get_list_stat


def wait_status(function, service: object, expected_status: int or str, delayed_action: int, func_args: list = [],
                customer_type: str = None) -> bool:
    timeout = time.time() + DELAY_SEC_SHORT
    while True:
        response = function(service, *func_args)
        if response == {}:
            raise Exception('Пришел пустой response')
        elif response.get('status') or response.get(customer_type).get('status') == expected_status:
            return True

        if time.time() > timeout:
            raise Exception('Не удалось получить ожидаемый статус')
        else:
            time.sleep(delayed_action)


def wait_customer_state(customer_gw, state, contract_signed=False, suspend=None, admin=None, frozen=None,
                        terminated_by=None, delay=DELAY_SEC_SHORT) -> bool:
    timeout = time.time() + delay
    while True:
        if help_get_state(customer_gw).get('state') == customer_state_int[state]:
            if state == 'CUSTOMER_STATE_ACTIVE' and help_get_state(customer_gw).get(
                    'contract_signed') == contract_signed:
                return True
            if state == 'CUSTOMER_STATE_BLOCKED':
                if suspend is not None and help_get_state(customer_gw).get('blocked').get('suspend') == suspend:
                    return True
                elif admin is not None and help_get_state(customer_gw).get('blocked').get('admin') == admin:
                    return True
                elif frozen is not None and help_get_state(customer_gw).get('blocked').get('frozen') == frozen:
                    return True
            if state == 'CUSTOMER_STATE_TERMINATED' and help_get_state(customer_gw).get('terminated').get(
                    'terminated_by') == terminated_by:
                return True

        if time.time() > timeout:
            raise Exception('Не удалось перевести кастомера в необходимый статус')
        else:
            time.sleep(1)


def wait_info(function, init_class: object, delayed_action: int, expected_info=None, grpc_stub: object = None,
              func_args: tuple = (), application_uuid: str = None, description: str = None,
              wait_status_code: bool = False, sleep: int = 0, wait_time=DELAY_SEC) -> bool:
    timeout = time.time() + wait_time
    time.sleep(sleep)
    while True:
        if grpc_stub:
            response = function(init_class, grpc_stub, *func_args)
            if wait_status_code is True:
                if response != StatusCode.NOT_FOUND:
                    return True
            elif check_grpc_method_response_content(response, expected_info, application_uuid, description) is True:
                return True

        elif grpc_stub is None:
            response = function(init_class, *func_args)
            if check_http_method_response_content(response, expected_info) is True:
                return True

        if time.time() > timeout:
            raise Exception('Не удалось получить ожидаемую информацию')

        else:
            time.sleep(delayed_action)


def wait_response_has_field(function, func_args: tuple, field: str, delayed_action: int, delay_sec: int = DELAY_SEC):
    timeout = time.time() + delay_sec
    while True:
        response = function(*func_args)
        if not isinstance(response, dict):
            response = response.json()
        if field in response.keys():
            return True
        if time.time() > timeout:
            raise Exception('Не удалось получить ожидаемую информацию')
        else:
            time.sleep(delayed_action)


def check_grpc_method_response_content(response, expected_info, application_uuid, description):
    if response == expected_info:
        return True
    elif response.get('action_history') and get_obj_list_from_objects_by_field_value(
            get_obj_list_from_objects_by_field_value(
                response.get('action_history'), "application_uuid", application_uuid),
            "description", description) != []:
        return True
    elif response.get('action_history') and get_obj_list_from_objects_by_field_value(
            response.get('action_history'), "description", description) != []:
        return True
    elif response.get('files_list'):
        return True
    else:
        return False


def check_http_method_response_content(response, expected_info):
    if response.json() == expected_info:
        return True
    elif response.json().get('resource_id') == expected_info:
        return True
    elif response.json().get('payments'):
        if sum([payment.get('sum') for payment in response.json().get('payments')]) == expected_info:
            return True
    else:
        return False


def waiting_sms_received(ms_gw, message_id, delay=DELAY_SEC_SHORT):
    timeout = time.time() + delay
    while True:
        response = help_get_list_ms(ms_gw=ms_gw)
        message_from_list = get_obj_list_from_objects_by_field_value(response.get("messages"),
                                                                     field_name="message_id",
                                                                     value=message_id)[0]
        if message_from_list is not None and message_from_list.get("status") == status_send_sms_int['STATUS_DELIVERED']:
            return True
        if message_from_list is not None and message_from_list.get("status") == status_send_sms_int['STATUS_FAILED']:
            raise Exception('Ошибка доставки')
        elif time.time() > timeout:
            raise Exception('Сообщение не было доставлено')


def waiting_statistics_call_id(statistics_gw, call_id, key_name):
    timeout = time.time() + DELAY_SEC
    while True:
        response = help_get_list_stat(
            statistics_gw=statistics_gw,
        ).get('calls')
        event = [event for event in response if event.get(key_name) == call_id]
        if event:
            return event[0]
        elif time.time() > timeout:
            raise Exception('Не удалось получить cписок евентов по приложению')
