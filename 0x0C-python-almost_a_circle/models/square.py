#!/usr/bin/python3
"""class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        sqr_str = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return sqr_str

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        attrs = ["id", "size", "x", "y"]
        new_dict = {}
        for i in attrs:
            new_dict[i] = getattr(self, i)
        return new_dict
