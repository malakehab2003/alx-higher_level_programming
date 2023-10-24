#!/usr/bin/python3
"""make a new class Square"""


class Square:
    """class of square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position
        if type(self.__position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(self.__position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
