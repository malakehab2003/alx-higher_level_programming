#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f"Last digit of {number} is ", end="")
if number > 0:
    last = number % 10
    print(f"{last} and is ", end="")
else:
    number = number * -1
    last = number % 10
    print(f"-{last} and is ", end="")
if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
else:
    print("less than 6 and not 0"i)
