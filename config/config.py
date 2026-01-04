import uuid


BASE_URL = "https://api-sandbox.y.uno/v1"

HEADERS = {
    "Content-Type": "application/json",
    "public-api-key": "<TO_BE_PROVIDED>",
    "private-secret-key": "<TO_BE_PROVIDED>",
    "x-idempotency-key": str(uuid.uuid4())
}


DEFAULT_PURCHASE_PAYLOAD = {
    "workflow": "DIRECT",         
    "amount": 1000,
    "currency": "USD",
    "account_id": "<TO_BE_PROVIDED>",
    "payment_method": {
        "type": "CARD",
        "card": {
            "number": "4111111111111111",
            "expiry_month": "12",
            "expiry_year": "2028",
            "cvv": "123"
        }
    }
}

DEFAULT_REFUND_PAYLOAD = {
    "amount": 1000,
    "reason": "Customer requested refund"
}

DEFAULT_AUTHORIZATION_PAYLOAD = {
    "workflow": "DIRECT",
    "amount": 1000,
    "currency": "USD",
    "account_id": "<TO_BE_PROVIDED>"
}



def refresh_idempotency_key():
    """
    Generates a new idempotency key for every request
    """
    HEADERS["x-idempotency-key"] = str(uuid.uuid4())
