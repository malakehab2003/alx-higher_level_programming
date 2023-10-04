#!/usr/bin/python3
i = 0
for num in range(122, 96, -1):
    if i % 2 != 0:
        new = num - 32
    else:
        new = num
    print("{}".format(chr(new)), end="")
    i += 1
