#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request"""
import sys
import requests


if __name__ == "__main__":
    param = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=param)
    print(r.text)
