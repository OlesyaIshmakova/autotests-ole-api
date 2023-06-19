import testit

from helpers.base_helpers import change_contract, to_base_64
from helpers.customer_gw.enum_helper import (contract_status_int,
                                             contract_type_int)
from helpers.generate_data import (EntrepreneurContractData,
                                   JuridicalContractData, PhysicalContractData)


@testit.step('Вызвать GetInfo - получить информацию о пользователе')
def help_get_customer_info_cgw(customer_gw):
    return customer_gw.get_customer_info().json()


@testit.step('Вызвать GetState - получить статусы кастомера')
def help_get_state(customer_gw):
    return customer_gw.get_customer_state().json()


@testit.step('Вызвать GetInfo - получить информацию о контракте')
def help_get_contract_info(customer_gw, contract_form):
    body = {"contract_form": contract_form}
    return customer_gw.get_contract_info(body).json()


@testit.step('Вызвать Create - создать бум. контракт ФЛ')
def help_create_contract_physical_paper(customer_gw):
    contract_data = PhysicalContractData().json_physical_contract_info
    contract_id = customer_gw.create_contract(json_data=contract_data).json().get("contract_id")
    change_contract(contract_data=contract_data,
                    customer_type='physical',
                    contract_id=contract_id,
                    status=contract_status_int['CONTRACT_STATUS_NOT_SIGNED'],
                    type=contract_type_int['CONTRACT_TYPE_PAPER'])
    return contract_data


@testit.step('Вызвать Create - создать бум. контракт ЮЛ')
def help_create_contract_juridical_paper(customer_gw, power_of_attorney=False):
    contract_data = JuridicalContractData().json_juridical_contract_info
    if power_of_attorney is False:
        signer = {
            "firstname": contract_data.get("juridical").get("contact").get("firstname"),
            "middlename": contract_data.get("juridical").get("contact").get("middlename"),
            "lastname": contract_data.get("juridical").get("contact").get("lastname"),
            "phone": contract_data.get("juridical").get("contact").get("phone")
        }
        change_contract(contract_data=contract_data,
                        customer_type='juridical',
                        signer=signer)
    contract_id = customer_gw.create_contract(json_data=contract_data).json().get("contract_id")
    change_contract(contract_data,
                    customer_type='juridical',
                    contract_id=contract_id,
                    status=contract_status_int['CONTRACT_STATUS_NOT_SIGNED'],
                    type=contract_type_int['CONTRACT_TYPE_PAPER'])
    return contract_data.get("juridical")


@testit.step('Вызвать Create - создать бум. контракт ИП')
def help_create_contract_entrepreneur_paper(customer_gw, power_of_attorney=False):
    contract_data = EntrepreneurContractData().json_entrepreneur_contract_info
    if power_of_attorney is False:
        signer = {
            "firstname": contract_data.get("entrepreneur").get("entrepreneur").get("firstname"),
            "middlename": contract_data.get("entrepreneur").get("entrepreneur").get("middlename"),
            "lastname": contract_data.get("entrepreneur").get("entrepreneur").get("lastname"),
            "phone": contract_data.get("entrepreneur").get("entrepreneur").get("phone")
        }
        change_contract(contract_data=contract_data,
                        customer_type='entrepreneur',
                        signer=signer)
    contract_id = customer_gw.create_contract(json_data=contract_data).json().get("contract_id")
    change_contract(contract_data=contract_data,
                    customer_type='entrepreneur',
                    contract_id=contract_id,
                    status=contract_status_int['CONTRACT_STATUS_NOT_SIGNED'],
                    type=contract_type_int['CONTRACT_TYPE_PAPER'])
    return contract_data.get("entrepreneur")


@testit.step('Вызвать Update - обновить данные контракта ФЛ')
def help_update_physical_contract(customer_gw, contract_id):
    contract_data = PhysicalContractData().json_physical_contract_info
    contract_data.get("physical").pop("payment_type")
    contract_data['contract_id'] = contract_id
    customer_gw.update_contract(json_data=contract_data).json()
    return contract_data


@testit.step('Вызвать Update - обновить данные контракта ЮЛ')
def help_update_juridical_contract(customer_gw, contract_id):
    contract_data = JuridicalContractData().json_juridical_contract_info
    contract_data.get("juridical").pop("payment_type")
    contract_data['contract_id'] = contract_id
    customer_gw.update_contract(json_data=contract_data).json()
    return contract_data


@testit.step('Вызвать Update - обновить данные контракта ИП')
def help_update_entrepreneur_contract(customer_gw, contract_id):
    contract_data = EntrepreneurContractData().json_entrepreneur_contract_info
    contract_data.get("entrepreneur").pop("payment_type")
    contract_data['contract_id'] = contract_id
    customer_gw.update_contract(json_data=contract_data).json()
    return contract_data


@testit.step('Вызвать Sign - подписать контракт ГУ')
def help_sign_contract(customer_gw):
    return customer_gw.sign_contract()


@testit.step('Вызвать Confirm - подтвердить контракт')
def help_confirm_contract(customer_gw, contract_id, contract_form):
    body = {"contract_id": contract_id,
            "contract_form": contract_form
            }
    return customer_gw.confirm_contract(body)


@testit.step('Вызвать ChangeLegalForm - изменить тип кастомера и способ подписания договора')
def help_change_legal_form(customer_gw, customer_type, sign_type, power_of_attorney=False):
    body = {
        "type": customer_type,
        "sign_type": sign_type,
        "power_of_attorney": power_of_attorney
    }
    return customer_gw.change_legal_form(json_data=body)


@testit.step('Вызвать SetPhoneNumber - установить номер телефона кастомера')
def help_set_phone_number(customer_gw, phone_number):
    body = {
        "phone_number": phone_number
    }
    return customer_gw.set_phone_number(json_data=body)


@testit.step('Вызвать SendSMSCode - отправить смс-код верификации')
def help_send_sms_code(customer_gw):
    return customer_gw.send_sms_code(json_data={}).json()


@testit.step('Вызвать метод SendDocuments - отправить документ в CRM')
def help_send_documents(customer_gw, document_type):
    documents = help_get_document_list_cgw(customer_gw).get('documents')
    document = [document for document in documents
                if document.get('document_type') == document_type]
    body = {
        "document_id": document[0].get('document_id'),
        "attachments": {
            "output-image.jpg": to_base_64('output-image.jpg')
        }
    }
    return customer_gw.send_documents(json_data=body).json()


@testit.step('Вызвать метод SendContract - отправить документ в CRM')
def help_send_contract(customer_gw, contract_id=None):
    contract_id = contract_id if contract_id else help_get_contract_list(customer_gw).get('contracts')[0].get(
        'contract_id')
    body = {
        "contract_id": contract_id,
        "attachments": {
            "output-image.jpg": to_base_64('output-image.jpg')
        }
    }
    return customer_gw.send_contract(json_data=body).json()


@testit.step('Вызвать GetDocumentList - получить список созданных слотов документов')
def help_get_document_list_cgw(customer_gw):
    return customer_gw.get_document_list({}).json()


@testit.step('Вызвать метод GetList - получение списка контрактов')
def help_get_contract_list(customer_gw):
    return customer_gw.get_contract_list(json_data={}).json()


@testit.step('Вызвать CheckSMSCode - проверить смс-код верификации')
def help_check_sms_code(customer_gw, sms_code):
    body = {
        "sms_code": sms_code
    }
    return customer_gw.check_sms_code(json_data=body).json()


@testit.step('Вызвать UpdateUserFlags - обновить флаги кастомера')
def help_update_user_flags(customer_gw, onboarding=None):
    body = {
        "user_flags": {
            "onboarding": onboarding
        }
    }
    return customer_gw.update_user_flags(json_data=body).json()
