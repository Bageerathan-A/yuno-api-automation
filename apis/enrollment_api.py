
from client.api_client import APIClient
from config.config import BASE_URL, HEADERS

class EnrollmentAPI:
    def __init__(self):
        self.client = APIClient(BASE_URL)

    def enroll_card(self, customer_id, payload=None, extra_headers=None):
        

        headers = HEADERS.copy()
        if extra_headers:
            headers.update(extra_headers)

        default_payload = {
            "customer_id": customer_id,
            "card_number": "4111111111111111",
            "expiry_month": "12",
            "expiry_year": "2028",
            "cvv": "123"
        }

        payload = payload or default_payload

        response = self.client.post(
            endpoint="/v1/enrollments",
            headers=headers,
            payload=payload
        )

        return response
