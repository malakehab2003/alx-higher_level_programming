#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    for char in str:
        if i == n:
            continue
        new[i] = char
        i += 1
    return new
