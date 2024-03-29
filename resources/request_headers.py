import requests
from .urls import CHALLENGER_URL


def get_x_challenger():
    request_get_challenger = requests.post(url=CHALLENGER_URL, json=None)
    x_challenger = request_get_challenger.headers.get("X-Challenger")
    return x_challenger


def get_headers():
    requests_header = {
        'X-CHALLENGER': f"{get_x_challenger()}",
        'Content-Type': 'application/json',
    }

    return requests_header
