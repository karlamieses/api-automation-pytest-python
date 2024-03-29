import requests
from resources.urls import BASE_URL


def fetch_data(url):
    try:
        response = requests.get(f"{BASE_URL}/todos")
        response.raise_for_status()
    except Exception as error:
        assert False, f"Request failed due to {error}"
    returned_data = response.json()
    return returned_data


def test_get_returns_all_to_do_list():
    returned_data = fetch_data(BASE_URL)
    returned_fields = returned_data["todos"][0]

    for _ in returned_fields:
        assert "id" in returned_fields
        assert "title" in returned_fields
        assert "doneStatus" in returned_fields
        assert "description" in returned_fields


def test_get_todo_list_with_id():
    returned_data = fetch_data(BASE_URL)

    try:
        get_id = returned_data["todos"][0]['id']
        response = requests.get(f"{BASE_URL}/todos/{get_id}")
        response.raise_for_status()
    except Exception as error:
        assert False, f"Request failed due to {error}"


def test_getting_an_id_that_does_not_exist():
    try:
        response = requests.get(f"{BASE_URL}/test")
    except Exception as error:
        assert False, f"Request failed {error}"

    assert response.status_code == 404




