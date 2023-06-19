import random

# import grpc
import pytest

# from clients.action_history_grpc_client import ActionHistoryClient
# from clients.apifonica_client import ApifonicaClient
# from clients.application_client import APPGWClient
# from clients.billing_clients.billing_account_grpc_client import \
#     BillingAccountClient
# from clients.billing_clients.billing_api_payment_grpc_client import \
#     BillingApiPaymentClient
# from clients.billing_clients.billing_application_grpc_client import \
#     BillingApplicationClient
# from clients.billing_clients.billing_call_record_client import BillingCallRecordClient
# from clients.billing_clients.billing_number_grpc_client import \
#     BillingNumberClient
# from clients.billing_clients.billing_payment_grpc_client import \
#     BillingPaymentClient
# from clients.billing_clients.billing_sip_grpc_client import BillingSipClient
# from clients.billing_clients.billing_tariff_grpc_client import \
#     BillingTariffClient
# from clients.bwl_gw_client import BWLGWClient
# from clients.call_back_client import CallBackGwClient
# from clients.call_gw_client import CallGwClient
# from clients.cma_client import CMAClient
# from clients.customer_gw_client import CGWClient
# from clients.docs_client import DocsClient
# from clients.event_service_client import EventServiceClient
# from clients.fs_client import FileStorageClient
# from clients.hlr_gw_client import HLRGWClient
# from clients.keycloak_client import KeyCloakClient
# from clients.lc_client import LcClient
# from clients.media_client import MediaGWClient
# from clients.messaging_client import MessagingGWClient
# from clients.nms_client import NMSClient
# from clients.nms_gui_client import NMSGuiClient
# from clients.numbers_client import NumbersGWClient
# from clients.portal_gw_client import PGWClient
# from clients.ri_client import ResourceInventoryClient
# from clients.smpp_client import SMPPClient
# from clients.statistics_gw_client import StatisticsGWClient
# from clients.verify_client import PublicVerifyClient
# from clients.verify_grpc_client import InternalVerifyClient
# from clients.voice_message_client import VoiceMessageGWClient
# from config import (ACTION_HISTORY_BASE_URL, ACTION_HISTORY_CERTIFICATE_NAME,
#                     AUTORESPONDER_WITH_FORWARDING,
#                     AUTORESPONDER_WITHOUT_FORWARDING,
#                     BILLING_API_PAYMENT_BASE_URL,
#                     BILLING_API_PAYMENT_CERTIFICATE_NAME, BILLING_BASE_URL,
#                     BILLING_CERTIFICATE_NAME, CERTIFICATE_PATH,
#                     CUSTOMER_BALANCE, EXOLVE_PASSWORD, EXOLVE_PASSWORD_1,
#                     EXOLVE_PASSWORD_2, EXOLVE_PASSWORD_3, EXOLVE_USER_NAME,
#                     EXOLVE_USER_NAME_1, EXOLVE_USER_NAME_2, EXOLVE_USER_NAME_3,
#                     FS_BASE_URL, FS_CERTIFICATE_NAME, REDIRECT_NUMBER,
#                     UVERIFIER_API_GRPC_BASE_URL, VERIFY_CERTIFICATE_NAME)
# from helpers.apifonica.apifonica_helper import help_update_number_info
# from helpers.application_gw.app_base_helper import (help_create_application,
#                                                     help_get_application_token,
#                                                     help_get_applications_list,
#                                                     help_terminate_application)
# from helpers.base_helpers import get_billing_number
# from helpers.billing.billing_base_helper import (help_get_sip,
#                                                  help_manual_payment)
# from helpers.billing.helper_functions import few_manual_payments
# from helpers.call_back_gw.call_back_base_helper import (help_create_call_back,
#                                                         help_delete_call_back)
# from helpers.call_gw.call_gw_base_helper import help_make_voice_message
# from helpers.cma.cma_base_helper import (
#     help_change_customer_contact_verification_status,
#     help_create_contract_physical_gos, help_get_customer_info_cma,
#     help_update_customer, refresh_customer_sign_type, refresh_customer_type)
# from helpers.cma.helper_functions import (clean_contracts,
#                                           refresh_customer_state)
# from helpers.customer_gw.cgw_base_helper import (
#     help_create_contract_entrepreneur_paper,
#     help_create_contract_juridical_paper)
from helpers.customer_gw.helper_functions import (
    create_not_signed_contract_juridical_paper,
    create_signed_contract_entrepreneur_gos,
    create_signed_contract_juridical_paper,
    create_signed_contract_physical_gos)
# from helpers.exolve_customer import ExolveCustomer
# from helpers.media_gw.mgw_base_helper import (help_delete_media,
#                                               help_get_list_media,
#                                               help_upload_media, media_files)
# from helpers.nms_hl.nms_hl_base_helpers import help_set_numbers_free
# from helpers.numbers_gw.nm_base_helpers import (help_buy_number,
#                                                 help_buy_random_number,
#                                                 help_create_sip,
#                                                 help_delete_call_forwarding,
#                                                 help_delete_sip,
#                                                 help_get_number_attributes,
#                                                 help_get_sip_list,
#                                                 search_random_number_code)
# from helpers.numbers_gw.nm_guide import (guid_category_ids, guide_region_ids,
#                                          guide_type_id)
# from helpers.portal_gw.portal_base_helper import help_get_balance_customer
# from helpers.voice_message_gw.vm_base_helpers import help_create_voice_message
# from helpers.waiting_functions import wait_info, waiting_statistics_call_id


@pytest.fixture(scope="session")
def user_account(worker_id):
    users = {
        "master": [EXOLVE_USER_NAME, EXOLVE_PASSWORD],
        "gw0": [EXOLVE_USER_NAME, EXOLVE_PASSWORD],
        "gw1": [EXOLVE_USER_NAME_1, EXOLVE_PASSWORD_1],
        "gw2": [EXOLVE_USER_NAME_2, EXOLVE_PASSWORD_2],
        "gw3": [EXOLVE_USER_NAME_3, EXOLVE_PASSWORD_3],
    }
    return {"username": users.get(worker_id)[0],
            "password": users.get(worker_id)[1]}


@pytest.fixture(scope="session")
def cma():
    return CMAClient()


@pytest.fixture(scope="session")
def docs():
    return DocsClient()


@pytest.fixture(scope="session")
def event_service():
    return EventServiceClient()


@pytest.fixture(scope="session")
def ri():
    return ResourceInventoryClient()


@pytest.fixture(scope="session")
def app_gw(user_account):
    return APPGWClient(user_account.get("username"), user_account.get("password"))


@pytest.fixture(scope='session')
def customer_gw(user_account):
    return CGWClient(user_account.get("username"), user_account.get("password"))


@pytest.fixture(scope='session')
def portal_gw(user_account):
    return PGWClient(user_account.get("username"), user_account.get("password"))


@pytest.fixture(scope='session')
def public_verify():
    return PublicVerifyClient()


@pytest.fixture(scope='session')
def key_cloak():
    return KeyCloakClient()


@pytest.fixture(scope='session')
def nms_gui():
    return NMSGuiClient()


@pytest.fixture(scope='session')
def nms():
    return NMSClient()


@pytest.fixture(scope='session')
def lc():
    return LcClient()


@pytest.fixture(scope='session')
def fs():
    return FileStorageClient()


@pytest.fixture(scope='session')
def call_gw(user_account):
    return CallGwClient(user_account.get("username"), user_account.get("password"))


@pytest.fixture(scope='session')
def apifonica():
    return ApifonicaClient()


@pytest.fixture(scope='session')
def billing_account():
    return BillingAccountClient()


@pytest.fixture(scope='session')
def billing_api_payment():
    return BillingApiPaymentClient()


@pytest.fixture(scope='session')
def billing_payment():
    return BillingPaymentClient()


@pytest.fixture(scope='session')
def billing_application():
    return BillingApplicationClient()


@pytest.fixture(scope='session')
def billing_call_record():
    return BillingCallRecordClient()


@pytest.fixture(scope='session')
def billing_number():
    return BillingNumberClient()


@pytest.fixture(scope='session')
def internal_verify():
    return InternalVerifyClient()


@pytest.fixture(scope='session')
def action_history():
    return ActionHistoryClient()


@pytest.fixture(scope='function')
def smpp():
    return SMPPClient()


@pytest.fixture(scope='session')
def billing_sip():
    return BillingSipClient()


@pytest.fixture(scope='session')
def billing_tariff():
    return BillingTariffClient()


@pytest.fixture(scope='package')
def grpc_stub_billing_account(grpc_stub_cls_billing_account, grpc_channel_billing):
    return grpc_stub_cls_billing_account(grpc_channel_billing)


@pytest.fixture(scope='package')
def grpc_stub_billing_api_payment(grpc_stub_cls_billing_api_payment, grpc_channel_billing_api_payment):
    return grpc_stub_cls_billing_api_payment(grpc_channel_billing_api_payment)


@pytest.fixture(scope='package')
def grpc_stub_billing_sip(grpc_stub_cls_billing_sip, grpc_channel_billing):
    return grpc_stub_cls_billing_sip(grpc_channel_billing)


@pytest.fixture(scope='package')
def grpc_stub_billing_application(grpc_stub_cls_billing_application, grpc_channel_billing):
    return grpc_stub_cls_billing_application(grpc_channel_billing)


@pytest.fixture(scope='package')
def grpc_stub_billing_call_record(grpc_stub_cls_billing_call_record, grpc_channel_billing):
    return grpc_stub_cls_billing_call_record(grpc_channel_billing)


@pytest.fixture(scope='package')
def grpc_stub_billing_number(grpc_stub_cls_billing_number, grpc_channel_billing):
    return grpc_stub_cls_billing_number(grpc_channel_billing)


@pytest.fixture(scope='package')
def grpc_stub_billing_tariff(grpc_stub_cls_billing_tariff, grpc_channel_billing):
    return grpc_stub_cls_billing_tariff(grpc_channel_billing)


@pytest.fixture(scope='package')
def grpc_stub_billing_payment(grpc_stub_cls_billing_payment, grpc_channel_billing):
    return grpc_stub_cls_billing_payment(grpc_channel_billing)


@pytest.fixture(scope='package')
def grpc_stub_filestorage(grpc_stub_cls_filestorage, grpc_channel_filestorage):
    return grpc_stub_cls_filestorage(grpc_channel_filestorage)


@pytest.fixture(scope='package')
def grpc_stub_action_history(grpc_stub_cls_action_history, grpc_channel_action_history):
    return grpc_stub_cls_action_history(grpc_channel_action_history)


@pytest.fixture(scope='package')
def grpc_stub_internal_verify(grpc_stub_cls_internal_verify, grpc_channel_internal_verify):
    return grpc_stub_cls_internal_verify(grpc_channel_internal_verify)


@pytest.fixture(scope='package')
def grpc_stub_cls_billing_account(grpc_channel_billing):
    from mtt.oliwio.billing.api_billing.account.v1.account_service_pb2_grpc import \
        AccountServiceStub
    return AccountServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_billing_api_billing(grpc_channel_billing):
    from mtt.oliwio.billing.api_billing.payment.v1.payment_service_pb2_grpc import \
        PaymentServiceStub
    return PaymentServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_billing_api_payment(grpc_channel_billing_api_payment):
    from mtt.oliwio.billing.api_payment.v1.payment_service_pb2_grpc import \
        PaymentServiceStub
    return PaymentServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_billing_sip(grpc_channel_billing):
    from mtt.oliwio.billing.api_billing.sip.v1.sip_service_pb2_grpc import \
        SIPServiceStub
    return SIPServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_billing_application(grpc_channel_billing):
    from mtt.oliwio.billing.api_billing.application.v1.application_service_pb2_grpc import \
        ApplicationServiceStub
    return ApplicationServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_billing_number(grpc_channel_billing):
    from mtt.oliwio.billing.api_billing.number.v1.number_service_pb2_grpc import \
        NumberServiceStub
    return NumberServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_billing_tariff(grpc_channel_billing):
    from mtt.oliwio.billing.api_billing.tariff.v1.tariff_service_pb2_grpc import \
        TariffServiceStub
    return TariffServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_billing_payment(grpc_channel_billing):
    from mtt.oliwio.billing.api_billing.payment.v1.payment_service_pb2_grpc import \
        PaymentServiceStub
    return PaymentServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_billing_call_record(grpc_channel_billing):
    from mtt.oliwio.billing.api_billing.call_record.v1.call_record_service_pb2_grpc import \
        CallRecordServiceStub
    return CallRecordServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_filestorage(grpc_channel_filestorage):
    from mtt.oliwio.filestorage.files_api.v1.files_api_service_pb2_grpc import \
        FilesApiServiceStub
    return FilesApiServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_action_history(grpc_channel_action_history):
    from mtt.oliwio.action_history.v1.action_history_service_pb2_grpc import \
        ActionHistoryServiceStub
    return ActionHistoryServiceStub


@pytest.fixture(scope='package')
def grpc_stub_cls_internal_verify(grpc_channel_internal_verify):
    from mtt.oliwio.user_verify.v1.internal_verify_service_pb2_grpc import \
        InternalVerifyServiceStub
    return InternalVerifyServiceStub


@pytest.fixture(scope='package')
def grpc_channel_billing():
    credential = grpc.ssl_channel_credentials(open(f'{CERTIFICATE_PATH}{BILLING_CERTIFICATE_NAME}', 'rb').read())
    with grpc.secure_channel(BILLING_BASE_URL, credential) as channel:
        yield channel


@pytest.fixture(scope='package')
def grpc_channel_billing_api_payment():
    credential = grpc.ssl_channel_credentials(open(f'{CERTIFICATE_PATH}'
                                                   f'{BILLING_API_PAYMENT_CERTIFICATE_NAME}', 'rb').read())
    with grpc.secure_channel(BILLING_API_PAYMENT_BASE_URL, credential) as channel:
        yield channel


@pytest.fixture(scope='package')
def grpc_channel_filestorage():
    credential = grpc.ssl_channel_credentials(open(f'{CERTIFICATE_PATH}{FS_CERTIFICATE_NAME}', 'rb').read())
    with grpc.secure_channel(FS_BASE_URL, credential) as channel:
        yield channel


@pytest.fixture(scope='package')
def grpc_channel_action_history():
    credential = grpc.ssl_channel_credentials(open(f'{CERTIFICATE_PATH}{ACTION_HISTORY_CERTIFICATE_NAME}', 'rb').read())
    with grpc.secure_channel(ACTION_HISTORY_BASE_URL, credential) as channel:
        yield channel


@pytest.fixture(scope='package')
def grpc_channel_internal_verify():
    credential = grpc.ssl_channel_credentials(open(f'{CERTIFICATE_PATH}{VERIFY_CERTIFICATE_NAME}', 'rb').read())
    with grpc.secure_channel(UVERIFIER_API_GRPC_BASE_URL, credential) as channel:
        yield channel


@pytest.fixture(scope="function")
def refresh_customer_state_to_active_signed(cma, customer_gw):
    refresh_customer_state(cma=cma,
                           customer_gw=customer_gw,
                           state='CUSTOMER_STATE_ACTIVE',
                           contract_signed=True,
                           username=customer_gw.username)


@pytest.fixture(scope="function")
def refresh_customer_state_to_active_signed_teardown(cma, customer_gw):
    yield
    refresh_customer_state(cma=cma,
                           customer_gw=customer_gw,
                           state='CUSTOMER_STATE_ACTIVE',
                           contract_signed=True,
                           username=customer_gw.username)


@pytest.fixture(scope="function")
def refresh_customer_state_to_active_not_signed(cma, customer_gw):
    refresh_customer_state(cma=cma,
                           customer_gw=customer_gw,
                           state='CUSTOMER_STATE_ACTIVE',
                           contract_signed=False,
                           username=customer_gw.username)


@pytest.fixture(scope="function")
def refresh_customer_state_to_active_not_signed_teardown(cma, customer_gw):
    yield
    refresh_customer_state(cma=cma,
                           customer_gw=customer_gw,
                           state='CUSTOMER_STATE_ACTIVE',
                           contract_signed=False,
                           username=customer_gw.username)


@pytest.fixture(scope="function")
def refresh_customer_type_to_physical(cma, user_account):
    refresh_customer_type(
        cma=cma,
        customer_type='CUSTOMER_TYPE_PHYSICAL',
        username=user_account.get("username"))


@pytest.fixture(scope="function")
def refresh_customer_type_to_juridical(cma, user_account):
    refresh_customer_type(
        cma=cma,
        customer_type='CUSTOMER_TYPE_JURIDICAL',
        username=user_account.get("username"))


@pytest.fixture(scope="function")
def refresh_customer_type_to_entrepreneur(cma, user_account):
    refresh_customer_type(
        cma=cma,
        customer_type='CUSTOMER_TYPE_ENTREPRENEUR',
        username=user_account.get("username"))


@pytest.fixture(scope="function")
def refresh_customer_sign_type_to_gos(cma, user_account):
    refresh_customer_sign_type(
        cma=cma,
        sign_type='CUSTOMER_SIGN_TYPE_GOS',
        username=user_account.get("username"))


@pytest.fixture(scope="function")
def refresh_customer_sign_type_to_paper(cma, user_account):
    refresh_customer_sign_type(
        cma=cma,
        sign_type='CUSTOMER_SIGN_TYPE_PAPER',
        username=user_account.get("username"))


@pytest.fixture(scope='function')
def clean_all_contracts(customer_gw, cma):
    clean_contracts(customer_gw, cma)


@pytest.fixture(scope='function')
def clean_all_contracts_teardown(customer_gw, cma):
    yield
    clean_contracts(customer_gw, cma)


@pytest.fixture(scope='package')
def communication_services(user_account, create_and_delete_app):
    application_uuid = create_and_delete_app
    username = user_account.get("username")
    password = user_account.get("password")
    return {
        'call_back_gw': CallBackGwClient(username, password, application_uuid=application_uuid),
        'nm_gw': NumbersGWClient(username, password, application_uuid=application_uuid),
        'm_gw': MediaGWClient(username, password, application_uuid=application_uuid),
        'vm_gw': VoiceMessageGWClient(username, password, application_uuid=application_uuid),
        "ms_gw": MessagingGWClient(username, password, application_uuid=application_uuid),
        "call_gw": CallGwClient(username, password, application_uuid=application_uuid),
        "bwl_gw": BWLGWClient(username, password, application_uuid=application_uuid),
        "portal_gw": PGWClient(username, password, application_uuid=application_uuid),
        "statistics_gw": StatisticsGWClient(username, password, application_uuid=application_uuid),
        "hlr_gw": HLRGWClient(username, password, application_uuid=application_uuid)
    }


@pytest.fixture(scope='package')
def create_and_delete_app(app_gw, request):
    application_uuid = help_create_application(app_gw).get('application_uuid')

    def _del_app():
        help_terminate_application(app_gw, application_uuid)

    request.addfinalizer(_del_app)
    return application_uuid


@pytest.fixture(scope='session', autouse=True)
def delete_all_apps_session(app_gw, cma, customer_gw):
    yield
    applications = help_get_applications_list(app_gw).get('applications')
    if applications:
        refresh_customer_state(
            cma=cma,
            customer_gw=customer_gw,
            state='CUSTOMER_STATE_ACTIVE',
            contract_signed=True,
            username=app_gw.username)
        for app in applications:
            app_uuid = app.get('application_uuid')
            help_terminate_application(app_gw, app_uuid)


@pytest.fixture(scope='function')
def delete_all_apps(app_gw, cma, customer_gw):
    yield
    applications = help_get_applications_list(app_gw).get('applications')
    if applications:
        refresh_customer_state(
            cma=cma,
            customer_gw=customer_gw,
            state='CUSTOMER_STATE_ACTIVE',
            contract_signed=True,
            username=app_gw.username)
        for app in applications:
            app_uuid = app.get('application_uuid')
            help_terminate_application(app_gw, app_uuid)


@pytest.fixture(scope="class")
def create_and_delete_apps(app_gw, request):
    marker = request.node.get_closest_marker("num_apps")
    num_apps = marker.args[0]
    application_uuids = [help_create_application(app_gw).get('application_uuid') for _ in range(num_apps)]
    yield application_uuids
    for application_uuid in application_uuids:
        help_terminate_application(app_gw, application_uuid)


@pytest.fixture(scope="class")
def create_few_payments(grpc_stub_billing_payment, billing_payment, billing_api_payment, grpc_stub_billing_api_payment,
                        cma):
    def _create_payment(username, count_manual_payments):
        few_manual_payments(
            grpc_stub_billing_payment=grpc_stub_billing_payment,
            billing_payment=billing_payment,
            grpc_stub_billing_api_payment=grpc_stub_billing_api_payment,
            billing_api_payment=billing_api_payment,
            cma=cma,
            username=username,
            count=count_manual_payments
        )

    return _create_payment


@pytest.fixture(scope='function')
def exolve_customer(grpc_stub_billing_account, billing_account, cma, key_cloak, grpc_stub_billing_payment,
                    billing_payment):
    return ExolveCustomer(grpc_stub_billing_account, billing_account, cma, key_cloak, grpc_stub_billing_payment,
                          billing_payment)


@pytest.fixture(scope='class')
def exolve_customer_class(grpc_stub_billing_account, billing_account, cma, key_cloak,
                          grpc_stub_billing_payment, billing_payment):
    username, password = ExolveCustomer(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                        grpc_stub_billing_payment, billing_payment).create()
    portal_gw = PGWClient(username, password)
    customer_gw = CGWClient(username, password)
    yield {
        "username": username,
        "customer_gw": customer_gw,
        "portal_gw": portal_gw,
    }


@pytest.fixture(scope='class')
def create_new_customer_and_app_class(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                      grpc_stub_billing_payment, billing_payment):
    username, password = ExolveCustomer(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                        grpc_stub_billing_payment, billing_payment).create()
    app_gw = APPGWClient(username, password)
    portal_gw = PGWClient(username, password)
    customer_gw = CGWClient(username, password)
    application_uuid = help_create_application(app_gw).get("application_uuid")
    application_token = help_get_application_token(app_gw=app_gw, application_uuid=application_uuid)
    nm_gw = NumbersGWClient(username, password, app_token=application_token)
    yield {
        "username": username,
        "password": password,
        "app_gw": app_gw,
        "portal_gw": portal_gw,
        "nm_gw": nm_gw,
        "customer_gw": customer_gw,
    }
    refresh_customer_state(
        cma=cma,
        customer_gw=customer_gw,
        state='CUSTOMER_STATE_ACTIVE',
        contract_signed=True,
        username=username
    )
    help_terminate_application(app_gw, application_uuid)


@pytest.fixture(scope="function")
def create_new_customer_and_app(exolve_customer, cma, request) -> dict:
    marker_customer_type = request.node.get_closest_marker("new_customer_type")
    marker_sign_type = request.node.get_closest_marker("new_customer_sign_type")
    customer_type = marker_customer_type.args[0]
    sign_type = marker_sign_type.args[0]
    username, password = exolve_customer.create(
        customer_type=customer_type,
        sign_type=sign_type
    )
    app_gw = APPGWClient(username, password)
    portal_gw = PGWClient(username, password)
    customer_gw = CGWClient(username, password)
    application_uuid = help_create_application(app_gw).get("application_uuid")
    application_token = help_get_application_token(app_gw=app_gw, application_uuid=application_uuid)
    customer_info = help_get_customer_info_cma(cma, username)
    customer_id = customer_info.get('customer_id')
    customer_number = customer_info.get("phone")
    yield {
        "customer_id": customer_id,
        "application_uuid": application_uuid,
        "application_token": application_token,
        "customer_number": customer_number,
        "portal_gw": portal_gw,
        "customer_gw": customer_gw,
        "username": username,
        "password": password
    }
    refresh_customer_state(
        cma=cma,
        customer_gw=customer_gw,
        state='CUSTOMER_STATE_ACTIVE',
        contract_signed=True,
        username=username
    )
    help_terminate_application(app_gw, application_uuid)


@pytest.fixture(scope='class')
def create_physical_customer_contract_signed(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                             grpc_stub_billing_payment, billing_payment,
                                             fs, grpc_stub_filestorage):
    exolve_customer = ExolveCustomer(grpc_stub_billing_account,
                                     billing_account, cma, key_cloak,
                                     grpc_stub_billing_payment, billing_payment)
    username, password = exolve_customer.create(
        customer_type="CUSTOMER_TYPE_PHYSICAL",
        sign_type="CUSTOMER_SIGN_TYPE_GOS"
    )
    app_gw = APPGWClient(username, password)
    portal_gw = PGWClient(username, password)
    customer_gw = CGWClient(username, password)
    statistics_gw = StatisticsGWClient(username, password)
    contract_data = create_signed_contract_physical_gos(cma, customer_gw, fs, grpc_stub_filestorage, username)
    yield {
        "username": username,
        "app_gw": app_gw,
        "portal_gw": portal_gw,
        "customer_gw": customer_gw,
        "statistics_gw": statistics_gw,
        "contract_data": contract_data
    }


@pytest.fixture(scope='class')
def create_physical_customer_contract_not_signed(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                                 grpc_stub_billing_payment, billing_payment,
                                                 fs, grpc_stub_filestorage):
    exolve_customer = ExolveCustomer(grpc_stub_billing_account,
                                     billing_account, cma, key_cloak,
                                     grpc_stub_billing_payment, billing_payment)
    username, password = exolve_customer.create(
        customer_type="CUSTOMER_TYPE_PHYSICAL",
        sign_type="CUSTOMER_SIGN_TYPE_GOS"
    )
    app_gw = APPGWClient(username, password)
    portal_gw = PGWClient(username, password)
    customer_gw = CGWClient(username, password)
    contract_data = help_create_contract_physical_gos(cma=cma, username=username)
    yield {
        "username": username,
        "app_gw": app_gw,
        "portal_gw": portal_gw,
        "customer_gw": customer_gw,
        "contract_data": contract_data
    }


@pytest.fixture(scope='class')
def create_entrepreneur_customer_contract_signed(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                                 grpc_stub_billing_payment, billing_payment,
                                                 fs, grpc_stub_filestorage):
    exolve_customer = ExolveCustomer(grpc_stub_billing_account,
                                     billing_account, cma, key_cloak,
                                     grpc_stub_billing_payment, billing_payment)
    username, password = exolve_customer.create(
        customer_type="CUSTOMER_TYPE_ENTREPRENEUR",
        sign_type="CUSTOMER_SIGN_TYPE_GOS"
    )
    app_gw = APPGWClient(username, password)
    portal_gw = PGWClient(username, password)
    customer_gw = CGWClient(username, password)
    contract_data = create_signed_contract_entrepreneur_gos(cma, customer_gw, fs, grpc_stub_filestorage, username)
    yield {
        "username": username,
        "app_gw": app_gw,
        "portal_gw": portal_gw,
        "customer_gw": customer_gw,
        "contract_data": contract_data
    }


@pytest.fixture(scope='class')
def create_juridical_customer_contract_signed(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                              grpc_stub_billing_payment, billing_payment, lc, docs,
                                              fs, grpc_stub_filestorage, internal_verify, grpc_stub_internal_verify,
                                              public_verify):
    exolve_customer = ExolveCustomer(grpc_stub_billing_account,
                                     billing_account, cma, key_cloak,
                                     grpc_stub_billing_payment, billing_payment)
    username, password = exolve_customer.create(
        customer_type='CUSTOMER_TYPE_JURIDICAL',
        sign_type='CUSTOMER_SIGN_TYPE_PAPER',
    )
    app_gw = APPGWClient(username, password)
    portal_gw = PGWClient(username, password)
    customer_gw = CGWClient(username, password)
    contract_data = create_signed_contract_juridical_paper(cma, lc, customer_gw, docs, fs, grpc_stub_filestorage,
                                                           username,
                                                           internal_verify, grpc_stub_internal_verify, verify_slot=3)
    return {
        "username": username,
        "app_gw": app_gw,
        "portal_gw": portal_gw,
        "customer_gw": customer_gw,
        "contract_data": contract_data
    }


@pytest.fixture(scope='class')
def create_juridical_customer_contract_not_signed(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                                  grpc_stub_billing_payment, billing_payment,
                                                  fs, grpc_stub_filestorage, internal_verify, grpc_stub_internal_verify,
                                                  public_verify):
    def _create_juridical_contract(verify_slot=3):
        exolve_customer = ExolveCustomer(grpc_stub_billing_account,
                                         billing_account, cma, key_cloak,
                                         grpc_stub_billing_payment, billing_payment)
        username, password = exolve_customer.create(
            customer_type='CUSTOMER_TYPE_JURIDICAL',
            sign_type='CUSTOMER_SIGN_TYPE_PAPER',
        )
        app_gw = APPGWClient(username, password)
        portal_gw = PGWClient(username, password)
        customer_gw = CGWClient(username, password)
        contract_data = create_not_signed_contract_juridical_paper(customer_gw,
                                                                   internal_verify,
                                                                   grpc_stub_internal_verify,
                                                                   verify_slot=verify_slot)
        return {
            "username": username,
            "app_gw": app_gw,
            "portal_gw": portal_gw,
            "customer_gw": customer_gw,
            "contract_data": contract_data
        }

    return _create_juridical_contract


@pytest.fixture(scope="module")
def create_juridical_customer_with_paper_sign_type(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                                   grpc_stub_billing_payment, billing_payment, internal_verify,
                                                   grpc_stub_internal_verify, ):
    exolve_customer = ExolveCustomer(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                     grpc_stub_billing_payment, billing_payment)
    username, password = exolve_customer.create(
        customer_type="CUSTOMER_TYPE_JURIDICAL",
        sign_type="CUSTOMER_SIGN_TYPE_PAPER"
    )
    customer_gw = CGWClient(
        username=username,
        password=password
    )
    contract_info = help_create_contract_juridical_paper(customer_gw)
    return {
        "customer_gw": customer_gw,
        "contract_id": contract_info.get('contract_id'),
        "contract_data": contract_info
    }


@pytest.fixture(scope="module")
def create_entrepreneur_customer_with_paper_sign_type(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                                      grpc_stub_billing_payment, billing_payment):
    exolve_customer = ExolveCustomer(grpc_stub_billing_account, billing_account, cma, key_cloak,
                                     grpc_stub_billing_payment, billing_payment)
    username, password = exolve_customer.create(
        customer_type="CUSTOMER_TYPE_ENTREPRENEUR",
        sign_type="CUSTOMER_SIGN_TYPE_PAPER"
    )
    customer_gw = CGWClient(
        username=username,
        password=password
    )
    contract_info = help_create_contract_entrepreneur_paper(customer_gw)
    return {
        "customer_gw": customer_gw,
        "contract_id": contract_info.get('contract_id'),
        "contract_data": contract_info
    }


@pytest.fixture(scope='function')
def check_balance(portal_gw, billing_payment, grpc_stub_billing_payment, key_cloak):
    if help_get_balance_customer(portal_gw) < CUSTOMER_BALANCE:
        help_manual_payment(
            grpc_stub_billing_payment=grpc_stub_billing_payment,
            billing_payment=billing_payment,
            account_id=get_billing_number(key_cloak, portal_gw.username),
            amount=CUSTOMER_BALANCE
        )


@pytest.fixture(scope='session')
def remove_numbers_from_quarantine(nms_gui, worker_id):
    if worker_id == "gw0" or worker_id == "master":
        help_set_numbers_free(nms_gui)
    yield
    if worker_id == "gw4" or worker_id == "master":
        help_set_numbers_free(nms_gui)


@pytest.fixture(scope='function')
def clean_all_medias(communication_services, request):
    def _del_medias():
        media_gw = communication_services["m_gw"]
        media_list = help_get_list_media(media_gw).get("media_records")
        if media_list:
            resource_ids = [resource_id.get("resource_id") for resource_id in media_list]
            for resource_id in resource_ids:
                help_delete_media(media_gw, resource_id)

    request.addfinalizer(_del_medias)


@pytest.fixture(scope='package')
def clean_all_medias_package(communication_services):
    def _del_medias():
        media_gw = communication_services["m_gw"]
        media_list = help_get_list_media(media_gw).get("media_records")
        if media_list:
            resource_ids = [resource_id.get("resource_id") for resource_id in media_list]
            for resource_id in resource_ids:
                help_delete_media(media_gw, resource_id)

    yield _del_medias


@pytest.fixture(scope='package')
def create_and_delete_media(communication_services, clean_all_medias_package, request):
    media_gw = communication_services.get("m_gw")
    created_medias = {"FILE_TYPE_PREMEDIA": {}, "FILE_TYPE_IVR": {}}

    def _create_media(media_n="media_1", file_type='FILE_TYPE_IVR'):
        if media_n not in created_medias[file_type]:
            media_data = help_upload_media(media_gw=media_gw, full_name=media_files[media_n]["file_name"],
                                           file_extension=media_files[media_n]["file_name"][-3:], file_type=file_type)
            created_medias[file_type].update({media_n: media_data})
            return media_data
        else:
            return created_medias[file_type][media_n]

    yield _create_media
    if help_get_list_media(media_gw).get("media_records"):
        request.addfinalizer(clean_all_medias_package)


@pytest.fixture(scope='class')
def create_and_delete_medias(communication_services, clean_all_medias_package, request):
    marker = request.node.get_closest_marker("num_medias")
    num_medias = marker.args[0]
    media_gw = communication_services.get("m_gw")
    [help_upload_media(media_gw=media_gw) for _ in range(num_medias)]


@pytest.fixture(scope='package')
def buy_random_number_active_signed_customer(communication_services, cma, customer_gw, portal_gw,
                                             grpc_stub_billing_payment, billing_payment, key_cloak):
    if help_get_balance_customer(portal_gw) < CUSTOMER_BALANCE:
        help_manual_payment(
            grpc_stub_billing_payment=grpc_stub_billing_payment,
            billing_payment=billing_payment,
            account_id=get_billing_number(key_cloak, portal_gw.username),
            amount=CUSTOMER_BALANCE
        )
    refresh_customer_state(cma=cma,
                           customer_gw=customer_gw,
                           state='CUSTOMER_STATE_ACTIVE',
                           contract_signed=True,
                           username=customer_gw.username)
    nm_gw = communication_services.get('nm_gw')
    number_info = help_buy_random_number(nm_gw)
    return {
        "number_code": number_info.get('number_code'),
        "application_uuid": nm_gw.application_uuid,
        "nm_gw": nm_gw,
        "type_name": number_info.get('type_name'),
        "region_name": number_info.get('region_name'),
    }


@pytest.fixture(scope='module')
def get_random_free_number_info(communication_services):
    nm_gw = communication_services.get("nm_gw")
    nm_info = search_random_number_code(nm_gw)
    type_name = nm_info.get("type_name")
    return {
        "type_id": guide_type_id.get(nm_info.get("type_name")),
        "region_id": guide_region_ids[type_name].get(nm_info.get("region_name")),
        "category_id": guid_category_ids[type_name].get(nm_info.get("category_name")),
        "number_code": nm_info.get("number_code")
    }


@pytest.fixture(scope='package')
def create_sip(buy_random_number_active_signed_customer):
    nm_gw = buy_random_number_active_signed_customer.get('nm_gw')
    number_code = buy_random_number_active_signed_customer.get('number_code')
    sip_resource_id = help_create_sip(nm_gw, number_code).get('sip_resource_id')
    return {
        "number_code": number_code,
        "application_uuid": nm_gw.application_uuid,
        "sip_resource_id": sip_resource_id,
        "nm_gw": nm_gw
    }


@pytest.fixture(scope='class')
def create_callback(communication_services):
    call_back_gw = communication_services.get('call_back_gw')
    call_back_data = help_create_call_back(call_back_gw)
    return call_back_data


@pytest.fixture(scope="function")
def buy_two_numbers_for_different_apps(app_gw) -> dict:
    application_uuid_1 = help_create_application(app_gw).get("application_uuid")
    application_uuid_2 = help_create_application(app_gw).get("application_uuid")
    num_gw_1 = NumbersGWClient(app_gw.username, app_gw.password, application_uuid_1)
    num_gw_2 = NumbersGWClient(app_gw.username, app_gw.password, application_uuid_2)
    number_1 = help_buy_number(num_gw_1, search_random_number_code(num_gw_1, type_id="DEF").get('number_code'))
    number_2 = help_buy_number(num_gw_2, search_random_number_code(num_gw_1, type_id="DEF").get('number_code'))
    yield [{"application_uuid": application_uuid_1,
            "number": number_1},
           {"application_uuid": application_uuid_2,
            "number": number_2}]
    help_terminate_application(app_gw, application_uuid_1)
    help_terminate_application(app_gw, application_uuid_2)


@pytest.fixture(scope="function")
def buy_number_for_new_customer(create_new_customer_and_app):
    new_customer = create_new_customer_and_app
    application_token = new_customer.get("application_token")
    num_gw = NumbersGWClient(new_customer.get("username"),
                             new_customer.get("password"),
                             app_token=application_token)
    bought_number = help_buy_number(num_gw, search_random_number_code(num_gw, type_id="DEF").get('number_code'))
    return bought_number


@pytest.fixture(scope='package')
def create_voice_message_without_redirect(create_and_delete_media, communication_services):
    vm_gw = communication_services.get("vm_gw")
    resource_id = create_and_delete_media().get("resource_id")
    return help_create_voice_message(
        vm_gw=vm_gw,
        resource_id=resource_id
    )


@pytest.fixture(scope='package')
def create_voice_message_with_redirect(create_and_delete_media, communication_services):
    vm_gw = communication_services.get("vm_gw")
    resource_id = create_and_delete_media().get("resource_id")
    return help_create_voice_message(
        vm_gw=vm_gw,
        resource_id=resource_id,
        redirect=True,
        redirect_number=REDIRECT_NUMBER
    )


@pytest.fixture(scope='package')
def set_gateway_id_3_in_apifonica(apifonica):
    def _set_gateway_id_3(number_code):
        help_update_number_info(
            apifonica=apifonica,
            number=number_code,
            gateway_id=3
        )

    return _set_gateway_id_3


@pytest.fixture(scope='package')
def make_voice_message_without_redirect(create_and_delete_media, cma, customer_gw, communication_services,
                                        set_gateway_id_3_in_apifonica, buy_random_number_active_signed_customer):
    vm_gw = communication_services.get("vm_gw")
    call_gw = communication_services.get("call_gw")
    resource_id = create_and_delete_media().get("resource_id")
    refresh_customer_state(
        cma=cma,
        customer_gw=customer_gw,
        state='CUSTOMER_STATE_ACTIVE',
        contract_signed=True,
        username=customer_gw.username)
    service_id = help_create_voice_message(
        vm_gw=vm_gw,
        resource_id=resource_id
    ).get('id')
    number_a = buy_random_number_active_signed_customer.get('number_code')
    number_b = random.choice(AUTORESPONDER_WITHOUT_FORWARDING)
    set_gateway_id_3_in_apifonica(number_a)
    customer_id = help_get_customer_info_cma(cma, call_gw.username).get('customer_id')
    help_change_customer_contact_verification_status(cma, customer_id=customer_id, type_contact="phone",
                                                     status=True)
    call_sid = help_make_voice_message(
        call_gw=call_gw,
        source=number_a,
        destination=number_b,
        service_id=service_id
    ).get('call_id')
    return {
        "number_a": number_a,
        "number_b": number_b,
        "call_sid": call_sid,

    }


@pytest.fixture(scope='class')
def make_few_voice_message(create_and_delete_media, cma, customer_gw, communication_services,
                           set_gateway_id_3_in_apifonica, buy_random_number_active_signed_customer, request):
    marker = request.node.get_closest_marker("num_vm")
    num_vm = marker.args[0]
    vm_gw = communication_services.get("vm_gw")
    statistics_gw = communication_services.get("statistics_gw")
    call_gw = communication_services.get("call_gw")
    call_sid_list = list()
    for _ in range(num_vm):
        resource_id = create_and_delete_media().get("resource_id")
        refresh_customer_state(
            cma=cma,
            customer_gw=customer_gw,
            state='CUSTOMER_STATE_ACTIVE',
            contract_signed=True,
            username=customer_gw.username)
        service_id = help_create_voice_message(
            vm_gw=vm_gw,
            resource_id=resource_id
        ).get('id')
        number_a = buy_random_number_active_signed_customer.get('number_code')
        number_b = random.choice(AUTORESPONDER_WITHOUT_FORWARDING)
        set_gateway_id_3_in_apifonica(number_a)
        customer_id = help_get_customer_info_cma(cma, call_gw.username).get('customer_id')
        help_change_customer_contact_verification_status(cma,
                                                         customer_id=customer_id,
                                                         type_contact="phone",
                                                         status=True)
        call_sid = help_make_voice_message(
            call_gw=call_gw,
            source=number_a,
            destination=number_b,
            service_id=service_id
        ).get('call_id')
        call_sid_list.append(call_sid)
    for call_sid in call_sid_list:
        waiting_statistics_call_id(statistics_gw, call_sid, 'call_sid')


@pytest.fixture(scope='package')
def make_voice_message_with_redirect(create_and_delete_media, communication_services,
                                     set_gateway_id_3_in_apifonica, buy_random_number_active_signed_customer):
    vm_gw = communication_services.get("vm_gw")
    call_gw = communication_services.get("call_gw")
    resource_id = create_and_delete_media().get("resource_id")
    service_id = help_create_voice_message(
        vm_gw=vm_gw,
        resource_id=resource_id,
        redirect=True,
        redirect_number=REDIRECT_NUMBER
    ).get('id')
    number_a = buy_random_number_active_signed_customer.get('number_code')
    number_b = random.choice(AUTORESPONDER_WITH_FORWARDING)
    set_gateway_id_3_in_apifonica(number_a)
    call_sid = help_make_voice_message(
        call_gw=call_gw,
        source=number_a,
        destination=number_b,
        service_id=service_id
    ).get('call_id')
    return {
        "number_a": number_a,
        "number_b": number_b,
        "call_sid": call_sid,
    }


@pytest.fixture(scope='package')
def make_two_voice_message_different_apps(app_gw, cma, create_and_delete_media, communication_services,
                                          set_gateway_id_3_in_apifonica, buy_random_number_active_signed_customer,
                                          make_voice_message_without_redirect):
    application_uuid_in_token = help_create_application(app_gw).get("application_uuid")
    vm_gw = VoiceMessageGWClient(app_gw.username, app_gw.password, application_uuid=application_uuid_in_token)
    call_gw = CallGwClient(app_gw.username, app_gw.password, application_uuid=application_uuid_in_token)
    media_gw = MediaGWClient(app_gw.username, app_gw.password, application_uuid=application_uuid_in_token)
    statistics_gw_1 = StatisticsGWClient(app_gw.username, app_gw.password, application_uuid=application_uuid_in_token)
    statistics_gw_1.headers = statistics_gw_1.headers_application
    nm_gw = NumbersGWClient(app_gw.username, app_gw.password, application_uuid=application_uuid_in_token)
    resource_id = help_upload_media(media_gw=media_gw).get("resource_id")
    service_id = help_create_voice_message(vm_gw=vm_gw, resource_id=resource_id).get('id')
    number_a = help_buy_random_number(nm_gw=nm_gw).get('number_code')
    set_gateway_id_3_in_apifonica(number_a)
    customer_id = help_get_customer_info_cma(cma, call_gw.username).get('customer_id')
    help_change_customer_contact_verification_status(cma, customer_id, "phone", status=True)
    call_sid_1 = help_make_voice_message(
        call_gw=call_gw,
        source=number_a,
        destination=random.choice(AUTORESPONDER_WITHOUT_FORWARDING),
        service_id=service_id
    ).get('call_id')
    waiting_statistics_call_id(statistics_gw_1, call_sid_1, 'call_sid')

    statistics_gw_2 = communication_services.get('statistics_gw')
    application_uuid_in_not_token = statistics_gw_2.application_uuid
    call_sid_2 = make_voice_message_without_redirect.get('call_sid')
    waiting_statistics_call_id(statistics_gw_2, call_sid_2, 'call_sid')
    return [
        {
            "application_uuid": application_uuid_in_token,
            'call_sid': call_sid_1,
            'statistics_gw': statistics_gw_1
        },
        {
            "application_uuid": application_uuid_in_not_token,
            'call_sid': call_sid_2,
            'statistics_gw': statistics_gw_2
        }
    ]


@pytest.fixture(scope="session", autouse=True)
def set_customer_user_type(cma, user_account):
    customer_id = help_get_customer_info_cma(cma, user_account.get("username")).get("customer_id")
    help_update_customer(cma=cma, customer_id=customer_id, user_type="CUSTOMER_USER_TYPE_AUTOTEST")


@pytest.fixture(scope='class')
def create_sips(communication_services, request):
    marker = request.node.get_closest_marker("num_sips")
    num_sips = marker.args[0]
    nm_gw = communication_services.get('nm_gw')
    list_sips_account = list()
    for i in range(num_sips):
        number_code = help_buy_random_number(nm_gw).get('number_code')
        sip_resource_id = help_create_sip(nm_gw, number_code).get('sip_resource_id')
        list_sips_account.append({
            "number_code": number_code,
            "application_uuid": nm_gw.application_uuid,
            "sip_resource_id": sip_resource_id,
            "nm_gw": nm_gw
        })
    return list_sips_account[::-1]


@pytest.fixture(scope='function')
def del_all_sips(communication_services, billing_sip, grpc_stub_billing_sip):
    yield
    nm_gw = communication_services.get('nm_gw')
    sips = help_get_sip_list(nm_gw).get('sips')
    if sips:
        for sip in sips:
            wait_info(
                function=help_get_sip,
                grpc_stub=grpc_stub_billing_sip,
                init_class=billing_sip,
                func_args=(sip.get('user_name'),),
                wait_status_code=True,
                delayed_action=7,
                expected_info={}
            )
            help_delete_sip(nm_gw, sip.get('sip_resource_id'))


@pytest.fixture(scope='class')
def create_and_delete_multiple_callbacks(communication_services, request):
    callback_gw = communication_services.get('call_back_gw')
    callbacks = []
    for i in range(request.param):
        callbacks.append(help_create_call_back(callback_gw).get('callback_resource_id'))
    yield
    for i in range(request.param):
        callbacks.append(help_delete_call_back(callback_gw, callbacks[i]))


@pytest.fixture(scope='function')
def del_call_forwarding(communication_services):
    nm_gw = communication_services.get('nm_gw')

    def _del_call_forwarding(number_code):
        call_forwarding_type = help_get_number_attributes(nm_gw, number_code).get(
            'attributes').get('call_forwarding_type')
        if call_forwarding_type:
            help_delete_call_forwarding(nm_gw, number_code)
    return _del_call_forwarding


@pytest.fixture(scope='function')
def verify_customer_contact(cma, user_account):
    customer_id = help_get_customer_info_cma(
        cma=cma,
        email=user_account.get("username")
    ).get('customer_id')
    help_change_customer_contact_verification_status(
        cma=cma,
        customer_id=customer_id,
        type_contact="phone",
        status=True
    )
