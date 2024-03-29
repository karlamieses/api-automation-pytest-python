import requests
from .urls import BASE_URL


def make_post_request(json_body, request_header):
    try:
        response = requests.post(f"{BASE_URL}/todos", json=json_body, headers=request_header)
        print(f"Created ToDo Item: {response.json()}")
    except Exception as error:
        assert False, f"Request failed due to: {error}"

    return response
