from client.api_client import APIClient
from config.config import BASE_URL, DEFAULT_PURCHASE_PAYLOAD, HEADERS


class PurchaseAPI:
    

    def __init__(self):
        self.client = APIClient(BASE_URL)

    def create_purchase(self, extra_payload=None, extra_headers=None):

        # Prepare payload
        payload = DEFAULT_PURCHASE_PAYLOAD.copy()
        if extra_payload:
            payload.update(extra_payload)

        # Prepare headers
        headers = HEADERS.copy()
        if extra_headers:
            headers.update(extra_headers)

        response = self.client.post(
            endpoint="/v1/payments",
            payload=payload,
            headers=headers
        )

        return response
