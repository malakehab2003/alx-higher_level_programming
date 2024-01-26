#!/usr/bin/python3
""" takes in a URL, sends a request to the URL"""
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as req:
        aim = req.info()
        id = aim.get('X-Request-Id')
        print(id)
