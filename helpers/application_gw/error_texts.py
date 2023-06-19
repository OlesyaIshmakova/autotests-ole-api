error_application_does_not_exist = 'Error scanning result: no rows in result set'
error_customer_status_blocked = 'all actions are forbidden for the blocked customer'
error_create_two_app_status_potential = 'customer in the status "potential" can create only one application'
error_terminate_app_status_potential = 'customer in the "potential" status cannot delete application'
error_value_length_must_between_1_or_40 = 'value length must be between 1 and 40 runes, inclusive'
error_value_length_must_be_at_most_90 = 'value length must be at most 90 runes'
error_invalid_uuid_format = 'value must be a valid UUID | caused by: invalid uuid format'
error_value_length_must_be_at_least_1 = 'value length must be at least 1 runes'
error_no_rows_in_result = 'Error scanning result: no rows in result set'
error_not_found = 'client or user not found'
error_out_of_range = 'out of range limit. Max limit - 100'
error_must_be_defined_enum = 'value must be one of the defined enum values'
error_value_must_be_absolute = 'value must be absolute'
error_value_must_be_a_valid_URI = 'value must be a valid URI'
error_missing_protocol_scheme = 'missing protocol scheme'


def error_create_application_already_exist(application_name):
    return f'ERROR: Application name [{application_name}] already exist (SQLSTATE AO026)'


def error_update_application_already_exist(application_name):
    return f'ERROR: Application name [{application_name}] alredy exists (SQLSTATE AO024)'


def error_update_resource_not_found(application_uuid):
    return f'ERROR: Application resource is not found pApplication_UUID = [{application_uuid}] (SQLSTATE AP004)'


def error_invalid_for_uint32(param_name):
    return f'invalid value for uint32 type: "{param_name}"'


def error_invalid_for_uint64(param_name):
    return f'invalid value for uint64 type: "{param_name}"'


def error_invalid_for_string(param_name):
    return f'invalid value for string type: {param_name}'


def error_invalid_for_enum(param_name):
    return f'invalid value for enum type: "{param_name}"'
