

from behave import given, when, then
from apis.customer_api import CustomerAPI
from config.config import HEADERS

customer_api = CustomerAPI()


@given("valid customer headers")
def step_valid_headers(context):
    context.headers = HEADERS.copy()



@when("I create a customer")
def step_create_customer(context):
    context.response = customer_api.create_customer(
        extra_headers=context.headers
    )


@when("I create a customer with extra payload")
def step_create_customer_extra(context):
    payload_overrides = {}
    if hasattr(context, "table"):
        for row in context.table:
            payload_overrides[row['name']] = row['value']

    context.response = customer_api.create_customer(
        payload=payload_overrides,
        extra_headers=context.headers
    )


@when("I create a customer with invalid email")
def step_customer_invalid_email(context):
    payload_overrides = {"email": "invalid_email"}
    context.response = customer_api.create_customer(
        payload=payload_overrides,
        extra_headers=context.headers
    )


@when("I create a customer without name")
def step_customer_missing_name(context):
    payload_overrides = {"name": None}
    context.response = customer_api.create_customer(
        payload=payload_overrides,
        extra_headers=context.headers
    )



@then("the response status should be {status}")
def step_verify_status(context, status):
    assert context.response.status_code == int(status), \
        f"Expected {status}, got {context.response.status_code}"
