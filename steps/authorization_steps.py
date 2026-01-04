

from behave import given, when, then
from apis.authorization_api import AuthorizationAPI
from config.config import HEADERS

auth_api = AuthorizationAPI()



@given("valid authorization headers")
def step_valid_headers(context):
    context.headers = HEADERS.copy()



@when("I authorize a payment")
def step_authorize_payment(context):
    context.response = auth_api.create_authorization(
        extra_headers=context.headers
    )


@when("I authorize a payment with extra payload")
def step_authorize_extra(context):
    payload_overrides = {}
    if hasattr(context, "table"):
        for row in context.table:
            payload_overrides[row['name']] = row['value']

    context.response = auth_api.create_authorization(
        extra_payload=payload_overrides,
        extra_headers=context.headers
    )


@when("I authorize payment with amount zero")
def step_authorize_zero_amount(context):
    payload_overrides = {"amount": 0}
    context.response = auth_api.create_authorization(
        extra_payload=payload_overrides,
        extra_headers=context.headers
    )


@when("I authorize payment with invalid card")
def step_authorize_invalid_card(context):
    payload_overrides = {
        "payment_method": {
            "type": "CARD",
            "card": {
                "number": "0000000000000000",
                "expiry_month": "01",
                "expiry_year": "2020",
                "cvv": "000"
            }
        }
    }
    context.response = auth_api.create_authorization(
        extra_payload=payload_overrides,
        extra_headers=context.headers
    )


@then("the response status should be {status}")
def step_verify_status(context, status):
    assert context.response.status_code == int(status), \
        f"Expected {status}, got {context.response.status_code}"
