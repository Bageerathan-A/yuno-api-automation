

from behave import given, when, then
from apis.enrollment_api import EnrollmentAPI
from config.config import HEADERS

enrollment_api = EnrollmentAPI()


@given("valid enrollment headers")
def step_valid_headers(context):
    context.headers = HEADERS.copy()



@when("I enroll a card for a customer")
def step_enroll_card(context):
    context.response = enrollment_api.enroll_card(
        customer_id="cust_001",
        extra_headers=context.headers
    )


@when("I enroll a card with extra payload")
def step_enroll_card_extra(context):
    payload_overrides = {}
    if hasattr(context, "table"):
        for row in context.table:
            payload_overrides[row['name']] = row['value']

    context.response = enrollment_api.enroll_card(
        customer_id=payload_overrides.get("customer_id", "cust_001"),
        payload=payload_overrides,
        extra_headers=context.headers
    )


@when("I enroll a card for invalid customer_id")
def step_enroll_invalid_customer(context):
    context.response = enrollment_api.enroll_card(
        customer_id="invalid_cust",
        extra_headers=context.headers
    )


@when("I enroll a card with expired card")
def step_enroll_expired_card(context):
    payload_overrides = {
        "card_number": "4111111111111111",
        "expiry_month": "01",
        "expiry_year": "2020",
        "cvv": "123"
    }
    context.response = enrollment_api.enroll_card(
        customer_id="cust_001",
        payload=payload_overrides,
        extra_headers=context.headers
    )



@then("the response status should be {status}")
def step_verify_status(context, status):
    assert context.response.status_code == int(status), \
        f"Expected {status}, got {context.response.status_code}"
