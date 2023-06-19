import testit

from clients.customer_gw_client import CGWClient
from config import TEST_BALANCE
from helpers.customer_gw.cgw_base_helper import help_change_legal_form
from helpers.generate_data import (generate_email, generate_password,
                                   generate_phone)


class ExolveCustomer:
    def __init__(self, grpc_stub_billing_account, billing_account, cma, key_cloak, grpc_stub_billing_payment,
                 billing_payment):
        self.grpc_stub_billing_account = grpc_stub_billing_account
        self.billing_account = billing_account
        self.grpc_stub_billing_payment = grpc_stub_billing_payment
        self.billing_payment = billing_payment
        self.cma = cma
        self.key_cloak = key_cloak
        self.username = generate_email()
        self.password = generate_password()

    def _register(self, user_type, phone):
        body = {
                "email": self.username,
                "user_type": user_type,
                "phone": phone
            }
        customer_id = self.cma.create_customer(json_data=body).json().get("customer_id")
        billing_number = self.billing_account.create(
            grpc_stub_billing_account=self.grpc_stub_billing_account,
        ).get("account_id")
        self.cma.update_customer_info(
            json_data={
                "customer_id": customer_id,
                "billing_number": billing_number
            }
        )
        self.key_cloak.registration_customer(username=self.username)
        return customer_id, billing_number

    def _update_password(self, customer_id, billing_number):
        user_id = self.key_cloak.get_user_info(
            email=self.username
        ).json()[0].get('id')
        self.key_cloak.reset_password(
            user_id=user_id,
            password=self.password
        )
        self.key_cloak.update_customer(
            user_id=user_id,
            customer_id=customer_id,
            billing_number=billing_number
        )

    def _replenish_test_balance(self, billing_number):
        self.billing_payment.manual_payment(
            grpc_stub_billing_payment=self.grpc_stub_billing_payment,
            account_id=int(billing_number),
            amount=TEST_BALANCE
        )

    @testit.step('Создать нового кастомера')
    def create(self,
               customer_type='CUSTOMER_TYPE_PHYSICAL',
               sign_type='CUSTOMER_SIGN_TYPE_GOS',
               user_type="CUSTOMER_USER_TYPE_AUTOTEST",
               power_of_attorney=False,
               phone=generate_phone()):
        customer_id, billing_number = self._register(user_type=user_type, phone=phone)
        self._update_password(
            customer_id=customer_id,
            billing_number=billing_number
        )
        self._replenish_test_balance(
            billing_number=billing_number
        )
        customer_gw = CGWClient(
            username=self.username,
            password=self.password
        )
        help_change_legal_form(
            customer_gw=customer_gw,
            customer_type=customer_type,
            sign_type=sign_type,
            power_of_attorney=power_of_attorney)
        return self.username, self.password
