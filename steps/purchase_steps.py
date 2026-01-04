
from behave import given, when, then
from apis.purchase_api import PurchaseAPI
from config.config import HEADERS, DEFAULT_PURCHASE_PAYLOAD

purchase_api = PurchaseAPI()

@given("valid purchase headers")
def step_valid_headers(context):
    context.headers = HEADERS.copy()

@when("I create a purchase")
def step_create_purchase(context):
    context.response = purchase_api.create_purchase(
        extra_headers=context.headers
    )


@when("I create a purchase with extra payload")
def step_create_purchase_extra(context):
    payload_overrides = {}
    if hasattr(context, "table"):
        for row in context.table:
            payload_overrides[row['name']] = row['value']

    context.response = purchase_api.create_purchase(
        extra_payload=payload_overrides,
        extra_headers=context.headers
    )


@when("I create a purchase with invalid card")
def step_create_invalid_card(context):
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
    context.response = purchase_api.create_purchase(
        extra_payload=payload_overrides,
        extra_headers=context.headers
    )


@when("I create a purchase with missing account id")
def step_create_missing_account(context):
    payload_overrides = {"account_id": None}
    context.response = purchase_api.create_purchase(
        extra_payload=payload_overrides,
        extra_headers=context.headers
    )


@then("the response status should be {status}")
def step_verify_status(context, status):
    assert context.response.status_code == int(status), \
        f"Expected {status}, got {context.response.status_code}"
