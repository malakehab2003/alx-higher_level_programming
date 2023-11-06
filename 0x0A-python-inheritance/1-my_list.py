#!/usr/bin/python3
"""make a new class my list"""


class MyList(list):
    """make the class to print the list"""

    def __init__(self):
        """inhert the super list"""
        super().__init__()

    def print_sorted(self):
        """print the list sorted acc"""
        print(sorted(self))
