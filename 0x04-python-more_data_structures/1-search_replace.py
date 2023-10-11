#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search <= 0:
        return my_list
    if search > len(my_list):
        return my_list
    new = my_list[:]
    for i in range(len(new)):
        if search == new[i]:
            new[i] = replace
    return new
