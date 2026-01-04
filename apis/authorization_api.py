from client.api_client import APIClient
from config.config import BASE_URL, HEADERS, DEFAULT_AUTHORIZATION_PAYLOAD


class AuthorizationAPI:
    def __init__(self):
        self.client = APIClient(BASE_URL)

    def create_authorization(self, extra_payload=None, extra_headers=None):
 

        payload = DEFAULT_AUTHORIZATION_PAYLOAD.copy()
        headers = HEADERS.copy()

        if extra_payload:
            payload.update(extra_payload)

        if extra_headers:
            headers.update(extra_headers)

        response = self.client.post(
            endpoint="/v1/payments",
            headers=headers,
            payload=payload
        )

        return response
