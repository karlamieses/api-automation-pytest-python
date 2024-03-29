import requests
from resources.urls import BASE_URL
from fixtures.post_queries import JsonBodies
from resources.post_utils import make_post_request
from resources.common import get_response_message, delete_created_item
from resources.request_headers import get_headers


requests_header = get_headers()


def test_post_a_valid_todo_list():
    response = make_post_request(JsonBodies.valid_post_format, requests_header)
    delete_created_item(response)


def test_post_a_todo_list_with_invalid_doneStatus():
    response = make_post_request(JsonBodies.invalid_doneStatus_type, requests_header)
    get_error_message = get_response_message(response)

    assert response.status_code == 400
    assert get_error_message == ['Failed Validation: doneStatus should be BOOLEAN but was STRING']


def test_post_a_todo_with_very_long_title():
    # Title allows only 50 characters
    response = make_post_request(JsonBodies.invalid_title_length, requests_header)

    get_error_message = get_response_message(response)

    assert response.status_code == 400
    assert get_error_message == [
        'Failed Validation: Maximum allowable length exceeded for title - maximum allowed is 50']


def test_post_a_todo_item_without_description_fields():
    response = make_post_request(JsonBodies.description_field_missing, requests_header)
    assert response.status_code == 201
    delete_created_item(response)


def test_post_a_todo_item_without_title_fields():
    response = make_post_request(JsonBodies.title_field_missing, requests_header)
    get_error_message = get_response_message(response)

    assert get_error_message == ['title : field is mandatory']


def test_post_a_todo_item_without_doneStatus_field():
    response = make_post_request(JsonBodies.doneStatus_field_missing, requests_header)

    assert response.status_code == 201
    delete_created_item(response)


def test_post_a_todo_item_with_unknown_field():
    response = make_post_request(JsonBodies.unknown_field_added, requests_header)
    get_error_message = get_response_message(response)

    assert get_error_message == ['Could not find field: unknown']


def test_an_item_can_be_updated_with_post():
    create_todo = make_post_request(JsonBodies.valid_post_format, requests_header)

    create_todo_data = create_todo.json()
    get_created_todo_id = create_todo_data["id"]

    print(f"The Created ID is: {get_created_todo_id}")

    edit_todo_json_body = {
        "title": "Update item with POST",
        "doneStatus": True,
        "description": ""
    }

    try:
        update_todo = requests.post(f"{BASE_URL}/todos/{get_created_todo_id}", json=edit_todo_json_body,
                                    headers=requests_header)
        print(f"Created ToDo Item: {update_todo.json()}")
    except Exception as error:
        assert False, f"Request failed due to: {error}"

    update_todo_data = update_todo.json()
    print(update_todo_data)
    get_updated_todo_id = update_todo_data["id"]
    get_updated_todo_title = update_todo_data["title"]

    assert get_updated_todo_id == get_created_todo_id
    assert get_updated_todo_title == "Update item with POST"

    print(f"The Updated ID is: {get_updated_todo_id}")

    delete_created_item(update_todo)