#!/usr/bin/python3
num = 97
for num in range(97, 123):
    if num == 113 or num == 101:
        continue
    print("{}".format(chr(num)), end="")
