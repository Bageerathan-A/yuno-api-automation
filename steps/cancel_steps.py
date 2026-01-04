
from behave import given, when, then
from apis.cancel_api import CancelAPI
from config.config import HEADERS

cancel_api = CancelAPI()



@given("valid cancel headers")
def step_valid_headers(context):
    context.headers = HEADERS.copy()



@when("I cancel the payment")
def step_cancel_payment(context):
    context.response = cancel_api.cancel_payment(
        payment_id="valid_payment_id",
        extra_headers=context.headers
    )


@when("I cancel payment with invalid payment_id")
def step_cancel_invalid(context):
    context.response = cancel_api.cancel_payment(
        payment_id="invalid_id",
        extra_headers=context.headers
    )


@when("I cancel a captured payment")
def step_cancel_captured(context):
    context.response = cancel_api.cancel_payment(
        payment_id="captured_payment_id",
        extra_headers=context.headers
    )


@then("the response status should be {status}")
def step_verify_status(context, status):
    assert context.response.status_code == int(status), \
        f"Expected {status}, got {context.response.status_code}"
