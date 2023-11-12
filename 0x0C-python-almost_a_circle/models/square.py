#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """get the attrs"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print data of square"""
        sqr_str = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return sqr_str

    @property
    def size(self):
        """get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attrs when added"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """get attrs as dict"""
        attrs = ["id", "size", "x", "y"]
        new_dict = {}
        for i in attrs:
            new_dict[i] = getattr(self, i)
        return new_dict
