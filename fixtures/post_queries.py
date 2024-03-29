class JsonBodies:
    valid_post_format = {
        "title": "go for a run",
        "doneStatus": True,
        "description": ""
    }

    invalid_doneStatus_type = {
        "title": "Post a todo list with doneStatus as string",
        "doneStatus": "true",  # This is a string instead of a boolean
        "description": ""
    }

    description_field_missing = {
        "title": "go for a run",
        "doneStatus": True
    }

    title_field_missing = {
        "doneStatus": True,
        "description": ""
    }

    doneStatus_field_missing = {
        "title": "Post a todo without doneStatus",
        "description": ""
    }

    invalid_title_length = {
        "title": "Post a todo list with a very long title as string. Post a todo list with a very long title as string. "
                 "Post a todo list with a very long title as string. Post a todo list with a very long title as string. "
                 "Post a todo list with a very long title as string. Post a todo list with a very long title as string. "
                 "Post a todo list with a very long title as string. Post a todo list with a very long title as string. "
                 "Post a todo list with a very long title as string. Post a todo list with a very long title as string. "
                 "Post a todo list with a very long title as string. Post a todo list with a very long title as string. "
                 "Post a todo list with a very long title as string. Post a todo list with a very long title as string. "
                 "Post a todo list with a very long title as string. Post a todo list with a very long title as string. ",
        "doneStatus": True,
        "description": ""
    }

    unknown_field_added = {
        "title": "Post a todo without doneStatus",
        "description": "",
        "unknown": True
    }


