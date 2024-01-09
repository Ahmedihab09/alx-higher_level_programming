#!/usr/bin/python3

'''to JSON string module'''


def to_json_string(my_obj):
    '''
    Returns a basic JSON representation of a simple Python dictionary object.
    This function does not handle complex or nested objects and is not a
    substitute for the json.dumps method.
    '''
    if isinstance(my_obj, dict):
        items = []
        for key, value in my_obj.items():
            json_key = str(key)
            if isinstance(value, str):
                json_value = '"' + value + '"'
            elif value is None:
                json_value = "null"
            elif isinstance(value, bool):
                json_value = "true" if value else "false"
            else:
                json_value = str(value)
            items.append(f'"{json_key}": {json_value}')
        json_string = "{" + ", ".join(items) + "}"
        return json_string
    else:
        raise TypeError("Object must be a dictionary")
