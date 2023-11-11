#!/usr/bin/python3
"""class rectangle"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y


        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            for f in range(self.__x):
                print("", end=" ")
            for j in range(self.__width):
                print("#", end='')
            print("")

    def __str__(self):
        rec_str = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return rec_str

    def update(self, *args, **kwargs):
        if args:
            attributes = ["id", "_Rectangle__width", 
                          "_Rectangle__height", "_Rectangle__x", "_Rectangle__y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        attrs = ["id", "width", "height", "x", "y"]
        new_dict = {}
        for i in attrs:
            new_dict[i] = getattr(self, i)
        return new_dict
        
