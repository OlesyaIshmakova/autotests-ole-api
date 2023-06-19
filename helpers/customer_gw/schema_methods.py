error_permission_denied = "permission denied: customer id in jwt token don't match customer id in contract"
error_text_confirm_fraud = 'client is fraud'
error_text_doc_list = "contragent ID is not found"
error_duplicate_contract = 'Duplicate Error'
error_text_customer_sign_type_gos = 'invalid customer sign type: only Gos sign type allowed'
error_text_customer_type_juridical = 'invalid customer type: only physical and entrepreneur clients allowed'
error_text_customer_type_physical = 'unknown field "physical"'
error_text_create_contract_customer_status = 'invalid customer status: only potential clients allowed'
error_text_create_contract_customer_have = 'customer already have contract'
error_failed_get_contract = 'failed to get contract info'
error_no_rows_in_result_set = 'scanning one: no rows in result set'
error_invalid_uuid_format = 'value must be a valid UUID | caused by: invalid uuid format'
error_unknown_account_type = 'unknown account type'
error_customer_number_not_found = 'customer number not found'
error_number_is_already_verified = 'number is already verified'
error_not_found_customer = 'Not found customer'
error_customer_already_have_legal_form = 'customer already have type, sign type and power of attorney'
error_user_flags_none = 'user_flags field must be non-nil'
error_changing_verified_number = 'changing verified number is not allowed'
error_changing_number_immediately = 'number cannot be changed until'
error_recreate_fraud_contract = 'impossible to create juridical contract because client is blocked'
error_not_found_enum_values = 'value must be one of the defined enum values'
error_invalid_value_for_enum_type = 'invalid value for enum type'
error_can_not_confirm_not_own_contract = "can't confirm not own contract"
error_contract_not_found = "failed to get customer contract: contracts not found"
error_customer_is_fraudster = "client is fraudster"
error_incorrect_destination_number = "can't send message to this number. Incorrect destination number"
error_too_many_requests = "too many requests, try again later"
error_already_signed = "invalid sign contract contract signed :true"
error_invalid_sign_contract = 'invalid sign contract - customer blocked, but not suspend'


def error_invalid_sms_code(count):
    return f'invalid code ({count}/3)'


def error_invalid_legal_form_combination(customer_type, sign_type, power_of_attorney):
    return f'input combination of type, sign_type and power_of_attorney is forbidden:' \
           f' {customer_type}, {sign_type}, {str(power_of_attorney).lower()}'


def error_invalid_phone_number(phone):
    return f'invalid phone number: {phone}'


def error_invalid_param_phone_number(param_name, phone):
    return f'invalid {param_name} phone number: {phone}'


def error_phone_not_match_regex_pattern(param_name):
    return f'{param_name}: value does not match regex pattern "(?i)^[0-9]+$"'


def error_value_length_must_between_9_or_14(param_name):
    return f'{param_name}: value length must be between 9 and 14 runes, inclusive'


def error_value_length_must_between_1_or_50(param_name):
    return f'{param_name}: value length must be between 1 and 50 runes, inclusive'


def error_value_length_must_between_1_or_10(param_name):
    return f'{param_name}: value length must be between 1 and 10 runes, inclusive'


def error_value_length_must_between_1_or_255(param_name):
    return f'{param_name}: value length must be between 1 and 255 runes, inclusive'


def error_value_length_must_between_1_or_20(param_name):
    return f'{param_name}: value length must be between 1 and 20 runes, inclusive'


def error_value_length_must_between_1_or_100(param_name):
    return f'{param_name}: value length must be between 1 and 100 runes, inclusive'


def error_value_length_must_between_1_or_8(param_name):
    return f'{param_name}: value length must be between 1 and 8 runes, inclusive'


def error_value_length_must_between_1_or_15(param_name):
    return f'{param_name}: value length must be between 1 and 15 runes, inclusive'


def error_value_length_must_between_1_or_4000(param_name):
    return f'{param_name}: value length must be between 1 and 4000 runes, inclusive'


def error_invalid_value_for_string_type(value):
    return f'invalid value for string type: {value}'


def error_invalid_value_for_int_type(value):
    return f'invalid value for int64 type: "{value}"'


def error_email_no_address(param_name):
    return f'{param_name}: value must be a valid email address | caused by: mail: no address'


def error_missing_dog_sign(param_name):
    return f"{param_name}: value must be a valid email address | caused by: mail: missing '@' or angle-addr"


def error_no_angle_addr(param_name):
    return f'{param_name}: value must be a valid email address | caused by: mail: no angle-addr'


def error_hostname_parts_cannot_begin_with_hyphens(param_name):
    return f'{param_name}: value must be a valid email address | caused by: hostname parts cannot begin with hyphens'


def error_value_length_must_be_n_runes(param_name, n):
    return f'{param_name}: value length must be {n} runes'


def error_param_contains_not_numeric_symbols(param_name):
    return f'{param_name} contains not numeric symbols'


def error_value_must_be_less_than_now(param_name):
    return f'{param_name}: value must be less than now'


def error_not_found_contract_id(contract_id):
    return f'Not found contract_id: {contract_id}'


def error_value_must_be_greater_than_0(param_name):
    return f'{param_name}: value must be greater than 0'


def error_customer_sign_type(customer_sign_type):
    return f'invalid customer sign type - {customer_sign_type}'


def error_create_contract_type_customer(expected_customer_type):
    return f'impossible to create {expected_customer_type} contract for non-{expected_customer_type} customer'


def error_customer_type(customer_sign_type):
    return f'invalid customer type: {customer_sign_type}'


def error_invalid_verification_status(status):
    return f'invalid sign contract verification status: {status}'


def error_contain_must_be_between(from_value, to_value):
    return f'value must contain between {from_value} and {to_value} pairs, inclusive'


def error_invalid_value(value_type, value) -> str:
    return f' invalid value for {value_type} type: {value}'


def error_param_length(value) -> str:
    return f'value length must be at least {value} bytes'


def error_value_is_required(param_name) -> str:
    return f'{param_name}: value is required'


def error_value_must_not_be_in_list(param_name) -> str:
    return f'{param_name}: value must not be in list [0]'
