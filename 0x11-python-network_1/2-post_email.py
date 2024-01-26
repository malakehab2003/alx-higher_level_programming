#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter"""
import sys
import urllib.request


if __name__ == "__main__":
    param = {'email': sys.argv[2]}
    url = sys.argv[1]
    querystr = urllib.parse.urlencode(param).encode("ascii")
    request = urllib.request.Request(url, querystr)
    with urllib.request.urlopen(request) as req:
        print(response.read().decode("utf-8"))
