# config.py - файл инициализации переменных из .env.<zone>
import os
from pathlib import Path

from dotenv import load_dotenv

environment = os.environ.get('ENV', 'pp')
env_path = Path('.') / f'.env.{environment}'

load_dotenv(dotenv_path=env_path)

# LOGGING
CURL: int = int(os.getenv('CURL'))

# BASE
DESCRIPTION_BASE = os.getenv('DESCRIPTION_BASE')

# EXOLVE
EXOLVE_BASE_URL = os.getenv('EXOLVE_BASE_URL')
EXOLVE_PASSWORD = os.getenv('EXOLVE_PASSWORD')
EXOLVE_USER_NAME = os.getenv('EXOLVE_USER_NAME')
NUMBER = os.getenv('NUMBER')

# MULTITHREADING MODE
EXOLVE_USER_NAME_1 = os.getenv('EXOLVE_USER_NAME_1')
EXOLVE_PASSWORD_1 = os.getenv('EXOLVE_PASSWORD_1')
EXOLVE_USER_NAME_2 = os.getenv('EXOLVE_USER_NAME_2')
EXOLVE_PASSWORD_2 = os.getenv('EXOLVE_PASSWORD_2')
EXOLVE_USER_NAME_3 = os.getenv('EXOLVE_USER_NAME_3')
EXOLVE_PASSWORD_3 = os.getenv('EXOLVE_PASSWORD_3')

# EXOLVE API
PUBLIC_GW_BASE_URL = os.getenv('PUBLIC_GW_BASE_URL')
CMA_BASE_URL = os.getenv('CMA_BASE_URL')
DOCS_BASE_URL = os.getenv('DOCS_BASE_URL')
UVERIFIER_API_BASE_URL = os.getenv('UVERIFIER_API_BASE_URL')
UVERIFIER_API_GRPC_BASE_URL = os.getenv('UVERIFIER_API_GRPC_BASE_URL')
BILLING_BASE_URL = os.getenv('BILLING_BASE_URL')
BILLING_API_PAYMENT_BASE_URL = os.getenv('BILLING_API_PAYMENT_BASE_URL')
FS_BASE_URL = os.getenv('FS_BASE_URL')
LC_BASE_URL = os.getenv('LC_BASE_URL')
ACTION_HISTORY_BASE_URL = os.getenv('ACTION_HISTORY_BASE_URL')
RI_BASE_URL = os.getenv('RI_BASE_URL')
S3_MINIO_BASE_URL = os.getenv('S3_MINIO_BASE_URL')

# # SMPP
# SMPP_HOST = os.getenv('SMPP_HOST')
# SMPP_PORT = int(os.getenv('SMPP_PORT'))
#
# # SIP
# SIP_DOMAIN = os.getenv('SIP_DOMAIN')
# SIP_SUBSCRIPTION_FEE = int(os.getenv('SIP_SUBSCRIPTION_FEE'))
# SIP_INSTALL_FEE = int(os.getenv('SIP_INSTALL_FEE'))

# KEYCLOAK
KEYCLOAK_URL = os.getenv('KEYCLOAK_URL')
KEYCLOAK_ADMIN_SECRET = os.getenv('KEYCLOAK_ADMIN_SECRET')
KEYCLOAK_GRANT_TYPE_CREDENTIALS = os.getenv('KEYCLOAK_GRANT_TYPE_CREDENTIALS')
KEYCLOAK_ADMIN_CLIENT = os.getenv('KEYCLOAK_ADMIN_CLIENT')
KEYCLOAK_USER_SECRET = os.getenv('KEYCLOAK_USER_SECRET')
KEYCLOAK_GRANT_TYPE_PASSWORD = os.getenv('KEYCLOAK_GRANT_TYPE_PASSWORD')
KEYCLOAK_USER_CLIENT = os.getenv('KEYCLOAK_USER_CLIENT')

# # NUMBER GW
# NM_TYPE_ID = os.getenv('NM_TYPE_ID')
# NM_REGION_ID = os.getenv('NM_REGION_ID')
# NM_CATEGORY_ID = os.getenv('NM_CATEGORY_ID')
# NM_DESCRIPTION_BUY_NUMBER = os.getenv('NM_DESCRIPTION_BUY_NUMBER')

# CUSTOMER GW
VERIFY_NUMBER = os.getenv('VERIFY_NUMBER')

# PORTAL GW
GET_DOC_DATE_FROM = os.getenv('GET_DOC_DATE_FROM')
GET_DOC_DATE_TO = os.getenv('GET_DOC_DATE_TO')
CUSTOMER_BALANCE = int(os.getenv('CUSTOMER_BALANCE'))
TEST_BALANCE = int(os.getenv('TEST_BALANCE'))

# # USER_VERIFY
# FRAUD_PHYSICAL_BIRTHDATE = os.getenv('FRAUD_PHYSICAL_BIRTHDATE')
# FRAUD_PHYSICAL_SERIAL = os.getenv('FRAUD_PHYSICAL_SERIAL')
# FRAUD_PHYSICAL_NUMBER = os.getenv('FRAUD_PHYSICAL_NUMBER')
# FRAUD_JURIDICAL_INN = os.getenv('FRAUD_JURIDICAL_INN')
# FRAUD_ENTREPRENEUR_INN = os.getenv('FRAUD_ENTREPRENEUR_INN')

# CALL_GW
# REDIRECT_NUMBER = os.getenv('REDIRECT_NUMBER')
#
# # NMS_HL
# NMS_URL = os.getenv('NMS_URL')
# NMS_GUI_URL = os.getenv('NMS_GUI_URL')
# NMS_LOGIN = os.getenv('NMS_LOGIN')
# NMS_PASSWORD = os.getenv('NMS_PASSWORD')
# NMS_STATE_ID = int(os.getenv('NMS_STATE_ID'))
# NMS_PROJECT_ID = int(os.getenv('NMS_PROJECT_ID'))
# NMS_CATEGORY_OWNER_ID = int(os.getenv('NMS_CATEGORY_OWNER_ID'))

# PAYMENT
# PAYMENT_URL = os.getenv('PAYMENT_URL')
# CURRENCY_PAYMENT = os.getenv('CURRENCY_PAYMENT')
# CURRENCY_EXOLVE = os.getenv('CURRENCY_EXOLVE')
# MERCHANT_ID_PHYSICAL = os.getenv('MERCHANT_ID_PHYSICAL')
# MERCHANT_ID_JURIDICAL = os.getenv('MERCHANT_ID_JURIDICAL')
# MERCHANT_ID_ENTREPRENEUR = os.getenv('MERCHANT_ID_ENTREPRENEUR')
#
# # EVENT SERVICE
# EVENT_SERVICE_URL = os.getenv('EVENT_SERVICE_URL')
#
# # APIFONICA
# APIFONICA_URL = os.getenv('APIFONICA_URL')
# APIFONICA_AUTH_TOKEN = os.getenv('APIFONICA_AUTH_TOKEN')
# AUTORESPONDER_WITHOUT_FORWARDING = list(os.getenv('AUTORESPONDER_WITHOUT_FORWARDING').split(','))
# AUTORESPONDER_WITH_FORWARDING = list(os.getenv('AUTORESPONDER_WITH_FORWARDING').split(','))
# SCENARIO_DROP_CALL = list(os.getenv('SCENARIO_DROP_CALL').split(','))
# SCENARIO_NOT_ANSWER = list(os.getenv('SCENARIO_NOT_ANSWER').split(','))
# SCENARIO_COMPLETED_CALL = list(os.getenv('SCENARIO_COMPLETED_CALL').split(','))
# SCENARIO_UNCOMPLETED_CALL = list(os.getenv('SCENARIO_UNCOMPLETED_CALL').split(','))
#
# DELAY_SEC = int(os.getenv('DELAY_SEC'))
# DELAY_SEC_SHORT = int(os.getenv('DELAY_SEC_SHORT'))
#
# BILLING_API_PAYMENT_CERTIFICATE_NAME = os.getenv('BILLING_API_PAYMENT_CERTIFICATE_NAME')
# BILLING_CERTIFICATE_NAME = os.getenv('BILLING_CERTIFICATE_NAME')
# ACTION_HISTORY_CERTIFICATE_NAME = os.getenv('ACTION_HISTORY_CERTIFICATE_NAME')
# VERIFY_CERTIFICATE_NAME = os.getenv('VERIFY_CERTIFICATE_NAME')
# FS_CERTIFICATE_NAME = os.getenv('FS_CERTIFICATE_NAME')
# CERTIFICATE_PATH = os.getenv('CERTIFICATE_PATH')
#
# MTT_EXOLVE = os.getenv('MTT_EXOLVE')
# MTT_EXOLVE_URL_RU = os.getenv('MTT_EXOLVE_URL_RU')
# MTT_EXOLVE_URL_EN = os.getenv('MTT_EXOLVE_URL_EN')
# MTT_SHORT = os.getenv('MTT_SHORT')
# MTT_COMPANY = os.getenv('MTT_COMPANY')
# MTT_ADDRESS = os.getenv('MTT_ADDRESS')
# MTT_ZIPCODE = os.getenv('MTT_ZIPCODE')
# MTT_OGRN = os.getenv('MTT_OGRN')
# MTT_INN = os.getenv('MTT_INN')
# MTT_KPP = os.getenv('MTT_KPP')
# MTT_ACCOUNT = os.getenv('MTT_ACCOUNT')
# MTT_BANK = os.getenv('MTT_BANK')
# MTT_CORR_ACCOUNT = os.getenv('MTT_CORR_ACCOUNT')
# MTT_BIK = os.getenv('MTT_BIK')
# MTT_PHONE = os.getenv('MTT_PHONE')
# MTT_EMAIL = os.getenv('MTT_EMAIL')
# MTT_FIO = os.getenv('MTT_FIO')
# MTT_DOV_NUMBER = os.getenv('MTT_DOV_NUMBER')
# MTT_DOV_DATE = os.getenv('MTT_DOV_DATE')
# SIGNED_ES = os.getenv('SIGNED_ES')
# ACCOUNTANT_FULLNAME = os.getenv('ACCOUNTANT_FULLNAME')
# ATTORNEY_SUPPORT = os.getenv('ATTORNEY_SUPPORT')
# LEADER_SUPPORT_FULLNAME = os.getenv('LEADER_SUPPORT_FULLNAME')
# VAT_RATE = int(os.getenv('VAT_RATE'))
#
# # SELENOID
# SELENOID_HOST = os.getenv('SELENOID_HOST')
#
# # RESOLUTION
# XL_height = os.getenv('XL_height')
# XL_width = os.getenv('XL_width')
