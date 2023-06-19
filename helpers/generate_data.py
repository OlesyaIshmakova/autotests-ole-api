import datetime
import random
from calendar import monthrange

from faker import Faker
from faker.providers.address import Provider as Address
from faker.providers.date_time import Provider as Date
from faker.providers.internet import Provider as Url
from faker.providers.phone_number import Provider as PhoneNumber

from clients.cma_client import CMAClient
from helpers.customer_gw.enum_helper import (contract_payment_type_int,
                                             personal_doc_type_int)

faker = Faker(locale="ru_RU")
phone_number = PhoneNumber(faker)
address = Address(faker)
date = Date(faker)
url = Url(faker)

def_codes = [900, 901, 902, 903, 904, 905, 906, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920,
             921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 936, 937, 938, 939, 941, 945,
             950, 951, 952, 953, 954, 955, 956, 958, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 977,
             978, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 991, 992, 993, 994, 995, 996, 997, 999]


def generate_now_datetime_in_utc(date_format="%Y-%m-%dT%H:%M:%SZ") -> dict:
    return dict(
        datetime=datetime.datetime.utcnow(),
        str_datetime=f'{datetime.datetime.strftime(datetime.datetime.utcnow(), date_format)}'
    )


def generate_now_datetime() -> datetime:
    return datetime.datetime.now()


def generate_now_date(format_date="%Y-%m-%dT%H:%M:%SZ") -> str:
    return f'{datetime.datetime.strftime(datetime.datetime.now(), format_date)}'


def generate_date_today(format_date="%d.%m.%Y") -> str:
    return datetime.datetime.strftime(datetime.datetime.now(), format_date)


def generate_count_days_on_month(month=datetime.datetime.now().month, year=datetime.datetime.now().year) -> int:
    return monthrange(
        year=year,
        month=month
    )[1]


def generate_first_day_on_past_month(date_format="%Y-%m-%dT%H:%M:%SZ") -> dict:
    day = datetime.datetime(
        year=datetime.datetime.now().year,
        month=datetime.datetime.now().month - 1,
        day=1
    )
    return dict(
        str_datetime=f'{datetime.datetime.strftime(day, date_format)}',
        datetime=day,
        date=day.date()
    )


def generate_last_day_on_past_month(date_format="%Y-%m-%dT%H:%M:%SZ") -> dict:
    count_days = generate_count_days_on_month(
        month=datetime.datetime.now().month - 1
    )
    day = datetime.datetime(
        year=datetime.datetime.now().year,
        month=datetime.datetime.now().month - 1,
        day=count_days
    )
    return dict(
        str_datetime=f'{datetime.datetime.strftime(day, date_format)}',
        datetime=day,
        date=day.date()
    )


def generate_first_day_on_next_month() -> dict:
    last_day = datetime.datetime(
        year=datetime.datetime.now().year,
        month=datetime.datetime.now().month + 1,
        day=1
    )
    return dict(
        datetime=last_day,
        date=last_day.date()
    )


def generate_past_datetime(timedelta=60) -> str:
    past_time = datetime.datetime.strftime(
        datetime.datetime.utcnow() - datetime.timedelta(minutes=timedelta),
        "%Y-%m-%dT%H:%M:%SZ"
    )
    return f'{past_time}'


def generate_future_datetime(timedelta=60) -> str:
    future_datetime = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(minutes=timedelta),
        "%Y-%m-%dT%H:%M:%SZ")
    return f'{future_datetime}'


def generate_phone() -> str:
    def_code = random.choice(def_codes)
    return '7' + str(def_code) + phone_number.phone_number().replace('-', '')[2:]


def generate_phone_with_incorrect_def_code() -> str:
    def_code = random.choice(list(set(range(900, 999)) - set(def_codes)))
    return '7' + str(def_code) + phone_number.phone_number().replace('-', '')[2:]


def generate_next_day() -> datetime:
    return datetime.datetime(
        year=generate_now_datetime().year,
        month=generate_now_datetime().month,
        day=generate_now_datetime().day + 1
    )


def generate_phones_list(count) -> list:
    phones_list = []
    for _ in range(count):
        phones_list.append(generate_phone())
    return phones_list


def generate_text(max_chars, min_chars=1) -> str:
    return faker.pystr(min_chars=min_chars, max_chars=max_chars)


def generate_ru_text(chars_count) -> str:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    chars = "".join(random.choice(alphabet) for _ in range(chars_count))
    return chars


def generate_spec_text(chars_count) -> str:
    chars = "".join(random.choice('~\\^') for _ in range(chars_count))
    return chars


def generate_sentence(max_words) -> str:
    return faker.sentence(nb_words=max_words, variable_nb_words=True)


def generate_email() -> str:
    return f'{generate_text(15)}@{faker.random_number(digits=7)}.{faker.tld()}'.lower()


def generate_password() -> str:
    return f'A{generate_text(min_chars=5, max_chars=5)}a{str(faker.random_number(digits=7))}'


def generate_int(min_value, max_value) -> str:
    return str(faker.pyint(min_value=min_value, max_value=max_value))


def generate_url(width=None, height=None, placeholder_url=None) -> str:
    return url.image_url(width=width, height=height, placeholder_url=placeholder_url)


def generate_uuid() -> str:
    return faker.uuid4()


def generate_events(values=True) -> dict:
    events = {
        "callback": generate_url() if values else '',
        "ipcr": generate_url() if values else '',
        "redirect": generate_url() if values else '',
        "sms": generate_url() if values else '',
        "voice_message": generate_url() if values else ''
    }
    return events


def generate_file_name(file_extension) -> str:
    return f'E2E_Test{generate_int(min_value=10, max_value=10000)}{generate_text(min_chars=10, max_chars=100)}.' \
           f'{file_extension}'


def get_random_question():
    cma = CMAClient()
    questions_info = cma.get_questions().json()
    questions_info = questions_info.get('questions')
    questions_info.remove({'question': 'None', 'question_id': 0})
    return random.choice([question for question in questions_info]).get('question_id')


class DocData:
    def __init__(self):
        super(DocData, self).__init__()
        self.json_doc_info = {
            'document_type': personal_doc_type_int['PERSONAL_DOC_TYPE_PASSPORT_RF'],
            "series": str(faker.random_number(digits=4)),
            "number": str(faker.random_number(digits=6)),
            "issuer": f'ГУ МВД по {faker.region()} {faker.city()}',
            "date": f'{date.iso8601(end_datetime=datetime.datetime.now())[:-8]}00:00:00Z',
            "country": faker.country()
        }


class PersonalData:
    def __init__(self):
        super(PersonalData, self).__init__()
        self.json_personal_info = {
            "phone": generate_phone(),
            "firstname": faker.first_name(),
            "middlename": faker.middle_name(),
            "lastname": faker.last_name(),
            "birthdate": f'{date.iso8601(end_datetime=datetime.datetime.now())[:-8]}00:00:00Z',
            "birthplace": faker.city()
        }


class AddressDate:
    def __init__(self):
        super(AddressDate, self).__init__()
        self.json_address_info = {
            "country": faker.country(),
            "zipcode": address.postcode(),
            "building": address.building_number(),
            "house": str(faker.random_number(digits=10)),
            "flat": str(faker.random_number(digits=50)),
            "frame": str(faker.random_number(digits=50)),
            "address": f'{faker.region()} {faker.city()} {faker.street_name()}'
        }


class SignerData:
    def __init__(self):
        super(SignerData, self).__init__()
        self.json_signer_info = {
            "firstname": faker.first_name(),
            "middlename": faker.middle_name(),
            "lastname": faker.last_name(),
            "phone": generate_phone()
        }


class ContactData:
    def __init__(self):
        super(ContactData, self).__init__()
        self.json_contact_info = {
            "firstname": faker.first_name(),
            "middlename": faker.middle_name(),
            "lastname": faker.last_name(),
            "email": faker.email(),
            "questions": get_random_question(),
            "phone": generate_phone()
        }


class BankDate:
    def __init__(self):
        super(BankDate, self).__init__()
        self.json_bank_info = {
            "name": faker.bank(),
            "account": faker.checking_account(),
            "corr_account": faker.correspondent_account(),
            "bik": faker.bic()
        }


class JuridicalData(BankDate):
    def __init__(self):
        super(JuridicalData, self).__init__()
        self.json_juridical_info = {
            "name": faker.company(),
            "inn": faker.businesses_inn(),
            "kpp": faker.kpp(),
            "ogrn": faker.businesses_ogrn(),
            "bank": self.json_bank_info
        }


class EntrepreneurData(BankDate):
    def __init__(self):
        super(EntrepreneurData, self).__init__()
        self.json_entrepreneur_info = {
            "name": f"ИП {faker.last_name()}",
            "firstname": faker.first_name(),
            "middlename": faker.middle_name(),
            "lastname": faker.last_name(),
            "phone": generate_phone(),
            "inn": faker.individuals_inn(),
            "ogrnip": faker.individuals_ogrn(),
            "bank": self.json_bank_info,
            "birthdate": f'{date.iso8601(end_datetime=datetime.datetime.now())[:-8]}00:00:00Z',
            "birthplace": faker.city()
        }


class PhysicalContractData(DocData, PersonalData, AddressDate):
    def __init__(self):
        super().__init__()
        self.json_physical_contract_info = {
            "physical": {
                "doc": self.json_doc_info,
                "addresses": {
                    "factual": self.json_address_info,
                    "postal": self.json_address_info,
                    "juridical": self.json_address_info,
                },
                "personal": self.json_personal_info,
                "payment_type": contract_payment_type_int["CONTRACT_PAYMENT_TYPE_ADVANCE"]
            }
        }


class JuridicalContractData(JuridicalData, SignerData, ContactData, AddressDate):
    def __init__(self):
        super().__init__()
        self.json_juridical_contract_info = {
            "juridical": {
                "juridical": self.json_juridical_info,
                "signer": self.json_signer_info,
                "contact": self.json_contact_info,
                "addresses": {
                    "juridical": self.json_address_info,
                    "factual": self.json_address_info,
                    "postal": self.json_address_info
                },
                "payment_type": contract_payment_type_int["CONTRACT_PAYMENT_TYPE_ADVANCE"]
            },
        }


class EntrepreneurContractData(DocData, EntrepreneurData, SignerData, ContactData, AddressDate):
    def __init__(self):
        super().__init__()
        self.json_entrepreneur_contract_info = {
            "entrepreneur": {
                "doc": self.json_doc_info,
                "entrepreneur": self.json_entrepreneur_info,
                "signer": self.json_signer_info,
                "contact": self.json_contact_info,
                "addresses": {
                    "factual": self.json_address_info,
                    "postal": self.json_address_info,
                    "juridical": self.json_address_info,
                },
                "payment_type": contract_payment_type_int["CONTRACT_PAYMENT_TYPE_ADVANCE"],
            }
        }
