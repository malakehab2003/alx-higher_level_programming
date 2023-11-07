#!/usr/bin/python3
"""write to json string"""
import json


def to_json_string(my_obj):
    """from dict. to json"""
    json_str = json.dumps(my_obj)
    return json_str
