#!/usr/bin/python3
"""class rectangle"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """private the data"""
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
        """get the width"""
        return self.__width

    @property
    def height(self):
        """get the height"""
        return self.__height

    @property
    def x(self):
        """get the x"""
        return self.__x

    @property
    def y(self):
        """get the y"""
        return self.__y

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set the x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set the y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """get the area"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle"""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            for f in range(self.__x):
                print("", end=" ")
            for j in range(self.__width):
                print("#", end='')
            print("")

    def __str__(self):
        """print data"""
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """update when got data"""
        if args:
            attributes = ["id", "_Rectangle__width",
                          "_Rectangle__height", "_Rectangle__x",
                          "_Rectangle__y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """make attrs to dict"""
        attrs = ["id", "width", "height", "x", "y"]
        new_dict = {}
        for i in attrs:
            new_dict[i] = getattr(self, i)
        return new_dict
