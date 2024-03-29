import requests
from .urls import BASE_URL


def get_response_message(response_request):
    returned_data = response_request.json()
    error_message = returned_data["errorMessages"]
    return error_message


def delete_created_item(request_response):
    returned_data = request_response.json()
    get_todo_id = returned_data["id"]
    print(f"Deleting ToDo item: {request_response.json()}")
    delete_response = requests.delete(f"{BASE_URL}/todos/{get_todo_id}")
    assert delete_response.status_code == 401
