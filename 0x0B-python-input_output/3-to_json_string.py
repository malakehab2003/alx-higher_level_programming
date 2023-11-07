#!/usr/bin/python3
"""write to json string"""
import json


def to_json_string(my_obj):
    json_str = json.dumps(my_obj)
    return json_str
