#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0:
        return 0
    i = 0
    count = 0
    x -= 1
    try:
        while i <= x:
            print("{}".format(my_list[i]), end="")
            i += 1
            count += 1
        print()
        return count
    except:
        print()
        return count
