#!/usr/bin/python3
"""from json string"""
import json


def from_json_string(my_str):
    """from json to data structure"""
    data_from_json = json.loads(my_str)
    return data_from_json
