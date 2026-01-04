

from behave import given, when, then
from apis.capture_api import CaptureAPI
from config.config import HEADERS

capture_api = CaptureAPI()



@given("valid capture headers")
def step_valid_headers(context):
    context.headers = HEADERS.copy()



@when("I capture the payment")
def step_capture_payment(context):
    context.response = capture_api.capture_payment(
        payment_id="valid_payment_id",
        extra_headers=context.headers
    )


@when("I capture payment with invalid payment_id")
def step_capture_invalid(context):
    context.response = capture_api.capture_payment(
        payment_id="invalid_id",
        extra_headers=context.headers
    )


@when("I capture payment without authorization")
def step_capture_without_auth(context):
    context.response = capture_api.capture_payment(
        payment_id=None,
        extra_headers=context.headers
    )


@then("the response status should be {status}")
def step_verify_status(context, status):
    assert context.response.status_code == int(status), \
        f"Expected {status}, got {context.response.status_code}"
