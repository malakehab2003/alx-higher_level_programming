#!/usr/bin/python3
for num in range(0, 9):
    num2 = num + 1
    for num2 in range(10):
        if num != 8 or num2 != 9:
            print("{}{}".format(num, num2), end=", ")
        else:
            print("{}{}".format(num, num2))
