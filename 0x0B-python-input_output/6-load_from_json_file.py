#!/usr/bin/python3
"""load from json file"""
import json


def load_from_json_file(filename):
    """load_from_json_file"""
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
