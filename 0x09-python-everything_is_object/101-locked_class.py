#!/usr/bin/python3
"""class with only one instanse"""


class LockedClass:
    """this class only accept the instanse first_name"""

    __slots__ = ["first_name"]
