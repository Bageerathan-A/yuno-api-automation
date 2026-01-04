

from behave import given, when, then
from apis.verify_api import VerifyAPI
from config.config import HEADERS

verify_api = VerifyAPI()



@given("valid verify headers")
def step_valid_headers(context):
    context.headers = HEADERS.copy()



@when("I verify the payment")
def step_verify_payment(context):
    context.response = verify_api.verify_payment(
        payment_id="valid_payment_id",
        extra_headers=context.headers
    )


@when("I verify payment with invalid payment_id")
def step_verify_invalid(context):
    context.response = verify_api.verify_payment(
        payment_id="invalid_id",
        extra_headers=context.headers
    )


@when("I verify payment that does not exist")
def step_verify_nonexistent(context):
    context.response = verify_api.verify_payment(
        payment_id="nonexistent_id",
        extra_headers=context.headers
    )



@then("the response status should be {status}")
def step_verify_status(context, status):
    assert context.response.status_code == int(status), \
        f"Expected {status}, got {context.response.status_code}"
