#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    high = list(a_dictionary.values())[0]
    target = list(a_dictionary.keys())[0]
    for key, value in a_dictionary.items():
        if value > high:
            high = value
            target = key
    return target
