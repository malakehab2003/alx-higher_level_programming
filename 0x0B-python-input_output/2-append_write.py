#!/usr/bin/python3
"""make write file function"""


def append_write(filename="", text=""):
    """write text in file"""
    counter = 0
    with open(filename, 'a', encoding='utf-8') as file:
        for letter in text:
            counter += 1
            file.write(letter)
    return counter
