#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            ord(c) =- 32
