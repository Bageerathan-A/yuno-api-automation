from client.api_client import APIClient
from config.config import BASE_URL, HEADERS

class CustomerAPI:
    def __init__(self):
        self.client = APIClient(BASE_URL)

    def create_customer(self, payload=None, extra_headers=None):
        
        headers = HEADERS.copy()
        if extra_headers:
            headers.update(extra_headers)

        # Default payload if none provided
        default_payload = {
            "name": "Test User",
            "email": "test@example.com"
        }

        payload = payload or default_payload

        response = self.client.post(
            endpoint="/v1/customers",
            headers=headers,
            payload=payload
        )

        return response
