import requests
import pytest



def test_1():
    response = requests.get()
    print(response.json())