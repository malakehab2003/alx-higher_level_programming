#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x <= 0:
        return 0
    i = 0
    count = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
        if i > 0:
            print("")
        return count
    except IndexError:
        print("")
        return count
