
from behave import given, when, then
from apis.refund_api import RefundAPI
from config.config import HEADERS

refund_api = RefundAPI()



@given("valid refund headers")
def step_valid_headers(context):
    context.headers = HEADERS.copy()



@when("I create a refund")
def step_create_refund(context):
    context.response = refund_api.create_refund(
        extra_headers=context.headers
    )


@when("I create a refund with extra payload")
def step_create_refund_extra(context):
    payload_overrides = {}
    if hasattr(context, "table"):
        for row in context.table:
            payload_overrides[row['name']] = row['value']

    context.response = refund_api.create_refund(
        extra_payload=payload_overrides,
        extra_headers=context.headers
    )


@when("I create a refund with excessive amount")
def step_refund_excess_amount(context):
    payload_overrides = {"amount": 100000}  # Excessive amount
    context.response = refund_api.create_refund(
        extra_payload=payload_overrides,
        extra_headers=context.headers
    )


@when("I create a refund with invalid payment id")
def step_refund_invalid_payment(context):
    payload_overrides = {"payment_id": "invalid_id"}
    context.response = refund_api.create_refund(
        extra_payload=payload_overrides,
        extra_headers=context.headers
    )



@then("the response status should be {status}")
def step_verify_status(context, status):
    assert context.response.status_code == int(status), \
        f"Expected {status}, got {context.response.status_code}"
