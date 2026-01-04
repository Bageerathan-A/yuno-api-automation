from client.api_client import APIClient
from config.config import BASE_URL, HEADERS, DEFAULT_CAPTURE_PAYLOAD


class CaptureAPI:
    def __init__(self):
        self.client = APIClient(BASE_URL)

    def capture_payment(self, payment_id, extra_payload=None, extra_headers=None):
        

        payload = DEFAULT_CAPTURE_PAYLOAD.copy()
        headers = HEADERS.copy()

       
        payload["payment_id"] = payment_id

        if extra_payload:
            payload.update(extra_payload)

        if extra_headers:
            headers.update(extra_headers)

        response = self.client.post(
            endpoint=f"/v1/payments/{payment_id}/capture",
            headers=headers,
            payload=payload
        )

        return response
