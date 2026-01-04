
from client.api_client import APIClient
from config.config import BASE_URL, HEADERS, DEFAULT_REFUND_PAYLOAD


class RefundAPI:
    def __init__(self):
        self.client = APIClient(BASE_URL)

    def create_refund(self, extra_payload=None, extra_headers=None):


        payload = DEFAULT_REFUND_PAYLOAD.copy()
        headers = HEADERS.copy()

        if extra_payload:
            payload.update(extra_payload)

        if extra_headers:
            headers.update(extra_headers)

        response = self.client.post(
            endpoint="/v1/refunds",
            headers=headers,
            payload=payload
        )

        return response
