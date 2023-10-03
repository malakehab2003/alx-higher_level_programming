#!/usr/bin/python3
for num in range(0, 9):
    for num2 in range(1, 10):
        num2 = num2 + num
        if num != 8 or num2 != 9:
            print("{}{}".format(num, num2), end=", ")
        else:
            print("{}{}".format(num, num2))
