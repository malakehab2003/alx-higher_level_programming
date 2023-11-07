#!/usr/bin/python3
"""make write file function"""


def write_file(filename="", text=""):
    """write text in file"""
    counter = 0
    with open(filename, 'w', encoding='utf-8') as file:
        for letter in text:
            counter += 1
            file.write(letter)
    return counter
