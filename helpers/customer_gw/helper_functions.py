from helpers.cma.cma_base_helper import (help_create_contract_entrepreneur_gos,
                                         help_create_contract_physical_gos,
                                         help_get_customer_info_cma,
                                         help_update_customer)
from helpers.customer_gw.cgw_base_helper import (
    help_confirm_contract, help_create_contract_entrepreneur_paper,
    help_create_contract_juridical_paper, help_get_contract_list,
    help_send_contract, help_send_documents, help_sign_contract)
from helpers.customer_gw.enum_helper import verify_slot_status_int
from helpers.docs.docs_base_helper import help_generate_contract
from helpers.docs.enum_helper import contract_status_docs_int
from helpers.fs.fs_base_helper import help_get_files_list
from helpers.lc.lc_helper import help_change_customer_status_lc
from helpers.u_verify.uverify_base_helper import (help_set_contract_resolution,
                                                  help_set_document_resolution)
from helpers.waiting_functions import wait_customer_state, wait_info


def create_signed_contract_physical_gos(cma, customer_gw, fs, grpc_stub_filestorage, username):
    contract_data = help_create_contract_physical_gos(cma=cma, username=username)
    customer_id = help_get_customer_info_cma(cma=cma, email=username).get("customer_id")
    help_update_customer(cma=cma,
                         customer_id=customer_id,
                         verification_status="CUSTOMER_VERIFICATION_STATUS_SUCCESS")
    help_sign_contract(customer_gw)
    wait_customer_state(
        customer_gw=customer_gw,
        state='CUSTOMER_STATE_ACTIVE',
        contract_signed=True,
        delay=45
    )
    wait_info(
        function=help_get_files_list,
        init_class=fs,
        grpc_stub=grpc_stub_filestorage,
        delayed_action=2,
        func_args=(int(customer_id),),
    )
    return contract_data


def create_signed_contract_entrepreneur_gos(cma, customer_gw, fs, grpc_stub_filestorage, username):
    contract_data = help_create_contract_entrepreneur_gos(cma=cma, username=username)
    customer_id = help_get_customer_info_cma(cma, email=username).get("customer_id")
    help_update_customer(cma=cma,
                         customer_id=customer_id,
                         verification_status="CUSTOMER_VERIFICATION_STATUS_SUCCESS")
    help_sign_contract(customer_gw)
    wait_customer_state(
        customer_gw=customer_gw,
        state='CUSTOMER_STATE_ACTIVE',
        contract_signed=True
    )
    wait_info(
        function=help_get_files_list,
        init_class=fs,
        grpc_stub=grpc_stub_filestorage,
        delayed_action=2,
        func_args=(int(customer_id),)
    )
    return contract_data


def create_not_signed_contract_entrepreneur_paper(customer_gw, internal_verify, grpc_stub_internal_verify,
                                                  verify_slot=1):
    contract_data = help_create_contract_entrepreneur_paper(customer_gw=customer_gw)
    contract_id = contract_data.get("contract_id")
    if verify_slot >= 1:
        help_confirm_contract(customer_gw, contract_id, contract_form='CONTRACT_FORM_ENTREPRENEUR')
        help_send_documents(customer_gw, 'DOCUMENT_INN')
        help_send_documents(customer_gw, 'DOCUMENT_OGRNIP')
        help_send_documents(customer_gw, 'DOCUMENT_PASSPORT_MAIN_PAGE')
        help_send_documents(customer_gw, 'DOCUMENT_PASSPORT_REGISTRATION_PAGE')
        help_send_documents(customer_gw, 'DOCUMENT_PASSPORT_WITH_SELFIE')
        help_set_document_resolution(
            internal_verify=internal_verify,
            customer_gw=customer_gw,
            grpc_stub_internal_verify=grpc_stub_internal_verify,
            document_type='DOCUMENT_INN',
            status=verify_slot_status_int['VERIFY_SLOT_STATUS_SUCCESS']
        )
        help_set_document_resolution(
            internal_verify=internal_verify,
            customer_gw=customer_gw,
            grpc_stub_internal_verify=grpc_stub_internal_verify,
            document_type='DOCUMENT_OGRNIP',
            status=verify_slot_status_int['VERIFY_SLOT_STATUS_SUCCESS']
        )
        help_set_document_resolution(
            internal_verify=internal_verify,
            customer_gw=customer_gw,
            grpc_stub_internal_verify=grpc_stub_internal_verify,
            document_type='DOCUMENT_PASSPORT_MAIN_PAGE',
            status=verify_slot_status_int['VERIFY_SLOT_STATUS_SUCCESS']
        )
        help_set_document_resolution(
            internal_verify=internal_verify,
            customer_gw=customer_gw,
            grpc_stub_internal_verify=grpc_stub_internal_verify,
            document_type='DOCUMENT_PASSPORT_REGISTRATION_PAGE',
            status=verify_slot_status_int['VERIFY_SLOT_STATUS_SUCCESS']
        )
        help_set_document_resolution(
            internal_verify=internal_verify,
            customer_gw=customer_gw,
            grpc_stub_internal_verify=grpc_stub_internal_verify,
            document_type='DOCUMENT_PASSPORT_WITH_SELFIE',
            status=verify_slot_status_int['VERIFY_SLOT_STATUS_SUCCESS']
        )
        if verify_slot > 1 or verify_slot == 2:
            contract_uuid = help_get_contract_list(customer_gw).get('contracts')[0].get(
                'contract_id')
            incident_id = help_send_contract(customer_gw, contract_id=contract_uuid).get('incident_id')

            if verify_slot > 2 or verify_slot == 3:
                help_set_contract_resolution(
                    internal_verify=internal_verify,
                    grpc_stub_internal_verify=grpc_stub_internal_verify,
                    contract_uuid=contract_uuid,
                    incident_id=incident_id
                )

    return contract_data


def create_not_signed_contract_juridical_paper(customer_gw, internal_verify,
                                               grpc_stub_internal_verify, verify_slot=1):
    contract_data = help_create_contract_juridical_paper(customer_gw)
    contract_id = contract_data.get("contract_id")
    if verify_slot >= 1:
        help_confirm_contract(customer_gw, contract_id, contract_form='CONTRACT_FORM_JURIDICAL')
        help_send_documents(customer_gw, 'DOCUMENT_INN')
        help_send_documents(customer_gw, 'DOCUMENT_OGRN')
        help_set_document_resolution(
            internal_verify=internal_verify,
            customer_gw=customer_gw,
            grpc_stub_internal_verify=grpc_stub_internal_verify,
            document_type='DOCUMENT_INN',
            status=verify_slot_status_int['VERIFY_SLOT_STATUS_SUCCESS']
        )
        help_set_document_resolution(
            internal_verify=internal_verify,
            customer_gw=customer_gw,
            grpc_stub_internal_verify=grpc_stub_internal_verify,
            document_type='DOCUMENT_OGRN',
            status=verify_slot_status_int['VERIFY_SLOT_STATUS_SUCCESS']
        )
        if verify_slot > 1 or verify_slot == 2:
            contract_uuid = help_get_contract_list(customer_gw).get('contracts')[0].get(
                'contract_id')
            incident_id = help_send_contract(customer_gw, contract_id=contract_uuid).get('incident_id')
            if verify_slot > 2 or verify_slot == 3:
                help_set_contract_resolution(
                    internal_verify=internal_verify,
                    grpc_stub_internal_verify=grpc_stub_internal_verify,
                    contract_uuid=contract_uuid,
                    incident_id=incident_id
                )
    return contract_data


def create_signed_contract_juridical_paper(cma, lc, customer_gw, docs, fs, grpc_stub_filestorage, username,
                                           internal_verify, grpc_stub_internal_verify, verify_slot=1):
    contract_data = help_create_contract_juridical_paper(customer_gw)
    contract_id = contract_data.get("contract_id")
    customer_id = help_get_customer_info_cma(cma, email=username).get("customer_id")
    billing_number = help_get_customer_info_cma(cma, email=username).get("billing_number")
    if verify_slot >= 1:
        help_confirm_contract(customer_gw, contract_id, contract_form='CONTRACT_FORM_JURIDICAL')
        help_send_documents(customer_gw, 'DOCUMENT_INN')
        help_send_documents(customer_gw, 'DOCUMENT_OGRN')
        help_set_document_resolution(
            internal_verify=internal_verify,
            customer_gw=customer_gw,
            grpc_stub_internal_verify=grpc_stub_internal_verify,
            document_type='DOCUMENT_INN',
            status=verify_slot_status_int['VERIFY_SLOT_STATUS_SUCCESS']
        )
        help_set_document_resolution(
            internal_verify=internal_verify,
            customer_gw=customer_gw,
            grpc_stub_internal_verify=grpc_stub_internal_verify,
            document_type='DOCUMENT_OGRN',
            status=verify_slot_status_int['VERIFY_SLOT_STATUS_SUCCESS']
        )
        if verify_slot > 1 or verify_slot == 2:
            contract_uuid = help_get_contract_list(customer_gw).get('contracts')[0].get(
                'contract_id')
            incident_id = help_send_contract(customer_gw, contract_id=contract_uuid).get('incident_id')
            if verify_slot > 2 or verify_slot == 3:
                help_set_contract_resolution(
                    internal_verify=internal_verify,
                    grpc_stub_internal_verify=grpc_stub_internal_verify,
                    contract_uuid=contract_uuid,
                    incident_id=incident_id
                )
                contract_data['status'] = contract_status_docs_int['CONTRACT_STATUS_SIGNED']
                help_generate_contract(docs, customer_id, 'CUSTOMER_TYPE_JURIDICAL', username, billing_number,
                                       juridical=contract_data)
                help_change_customer_status_lc(lc,
                                               billing_number=billing_number,
                                               customer_status='CUSTOMER_STATUS_COMMERCIAL')
                wait_info(
                    function=help_get_files_list,
                    init_class=fs,
                    grpc_stub=grpc_stub_filestorage,
                    delayed_action=2,
                    func_args=(int(customer_id),)
                )

    return contract_data


def del_option_param_in_contract(contract_data, contract_type):
    if contract_type == 'entrepreneur':
        contract_data['entrepreneur']['addresses'] = {}
        contract_data.get('entrepreneur').pop('signer')
        contract_data.get('entrepreneur').pop('contact')
        contract_data.get('entrepreneur').get('doc').pop('country')
        contract_data.get('entrepreneur').get('entrepreneur').pop('middlename')
        contract_data.get('entrepreneur').get('entrepreneur').pop('birthplace')
        contract_data.get('entrepreneur').get('entrepreneur').pop('bank')
        return contract_data
    elif contract_type == 'juridical':
        contract_data['juridical']['addresses'] = {}
        contract_data.get('juridical').pop('signer')
        contract_data.get('juridical').get('contact').pop('middlename')
        return contract_data
