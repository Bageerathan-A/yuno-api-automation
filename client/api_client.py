import requests
from config.config import HEADERS, refresh_idempotency_key


class APIClient:


    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, payload, headers=None):

        refresh_idempotency_key()

        url = f"{self.base_url}{endpoint}"
        request_headers = headers if headers else HEADERS

        response = requests.post(
            url=url,
            json=payload,
            headers=request_headers
        )
        return response

    def get(self, endpoint, headers=None):

        url = f"{self.base_url}{endpoint}"
        request_headers = headers if headers else HEADERS

        response = requests.get(
            url=url,
            headers=request_headers
        )
        return response

    def put(self, endpoint, payload=None, headers=None):

        url = f"{self.base_url}{endpoint}"
        request_headers = headers if headers else HEADERS

        response = requests.put(
            url=url,
            json=payload,
            headers=request_headers
        )
        return response

    def delete(self, endpoint, headers=None):
 
        url = f"{self.base_url}{endpoint}"
        request_headers = headers if headers else HEADERS

        response = requests.delete(
            url=url,
            headers=request_headers
        )
        return response
