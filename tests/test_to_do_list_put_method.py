import requests
from resources.urls import BASE_URL
from resources.post_utils import make_post_request
from resources.request_headers import get_headers
from fixtures.post_queries import JsonBodies
from resources.common import delete_created_item

requests_headers = get_headers()


def test_update_donestatus_of_a_todo_item_with_full_payload():
    edit_todo_json_body = {
        "title": "Update item with POST",
        "doneStatus": False,
        "description": ""
    }

    create_todo_item = make_post_request(JsonBodies.valid_post_format, requests_headers)
    created_item_data = create_todo_item.json()
    get_id = created_item_data["id"]

    update_item = requests.put(f"{BASE_URL}/todos/{get_id}", json=edit_todo_json_body, headers=requests_headers)

    updated_item_data = update_item.json()
    get_donestatus = updated_item_data["doneStatus"]

    assert get_donestatus == False

    delete_created_item(update_item)


def test_update_title_of_a_todo_item_with_partial_payload():
    edit_todo_json_body = {
        "title": "NEW TITLE",
    }

    create_todo_item = make_post_request(JsonBodies.valid_post_format, requests_headers)
    created_item_data = create_todo_item.json()
    get_id = created_item_data["id"]

    update_item = requests.put(f"{BASE_URL}/todos/{get_id}", json=edit_todo_json_body, headers=requests_headers)

    updated_item_data = update_item.json()
    get_donestatus = updated_item_data["doneStatus"]

    assert get_donestatus == False

    delete_created_item(update_item)
