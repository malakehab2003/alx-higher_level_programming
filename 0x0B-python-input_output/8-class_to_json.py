#!/usr/bin/python3
"""make class to json"""


def class_to_json(obj):
    """class to json"""
    if isinstance(obj, dict):
        return obj

    if hasattr(obj, '__dict__'):
        data = {}
        for key, value in obj.__dict__.items():
            if isinstance(value, (int, str, bool, list, dict)):
                data[key] = value
            elif isinstance(value, object):
                data[key] = class_to_json(value)
        return data

    return obj
