#!/usr/bin/python3
"""This module contains class square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ Override the __str__ method to return a specific string format """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.height)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
