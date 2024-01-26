#!/usr/bin/python3
""" takes in a URL, sends a request to the URL"""
import sys
import urllib.request


if __name__ == "__main__":
    try:
        request = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(request) as req:
            print(req.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
