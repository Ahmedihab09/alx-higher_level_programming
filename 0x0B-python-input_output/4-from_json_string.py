#!/usr/bin/python3

'''from JSON string module'''


def from_json_string(my_str):
    '''Returns an Python data structure represented by a JSON string'''
    import json
    return json.loads(my_str)
