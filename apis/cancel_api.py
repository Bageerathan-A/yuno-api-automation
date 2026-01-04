from client.api_client import APIClient
from config.config import BASE_URL, HEADERS

class CancelAPI:
    def __init__(self):
        self.client = APIClient(BASE_URL)

    def cancel_payment(self, payment_id, extra_headers=None):
        

        headers = HEADERS.copy()
        if extra_headers:
            headers.update(extra_headers)

        response = self.client.post(
            endpoint=f"/v1/payments/{payment_id}/cancel",
            headers=headers,
            payload={}  
        )

        return response
