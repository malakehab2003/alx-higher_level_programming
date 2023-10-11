#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    num = 0
    for i in new:
        num += i
    return num
