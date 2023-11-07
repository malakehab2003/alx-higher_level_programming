#!/usr/bin/python3
"""make function read_file"""


def read_file(filename=""):
    """read file and print it"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
