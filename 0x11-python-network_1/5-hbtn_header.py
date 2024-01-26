#!/usr/bin/python3
""" takes in a URL, sends a request to the URL"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
