#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    high = list(a_dictionary.values())[0]
    target = ""
    for key, value in a_dictionary.items():
        if value > high:
            high = value
            target = key
    return target
