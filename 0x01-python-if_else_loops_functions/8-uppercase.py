#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            val = ord(c)
            val -= 32
            c = chr(val)
        print("{}".format(c), end="")
    print("")
