#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    """ print format of url data"""
    req = request.urlopen("https://alx-intranet.hbtn.io/status")
    data = req.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('UTF-8')))
