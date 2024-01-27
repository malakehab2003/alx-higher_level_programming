#!/usr/bin/python3
""" takes in a letter and sends a POST request"""
import sys
import requests


if __name__ == "__main__":
    param = {"q": ""}
    if len(sys.argv) >= 2:
        param = {'q': sys.argv[1]}
    r = requests.post("http://0.0.0.0:5000/search_user", data=param)
    try:
        req = r.json()
        if req == {}:
            print("No result")
        else:
            print("[{}] {}".format(req.get("id"), req.get("name")))
    except ValueError:
        print("Not a valid JSON")
