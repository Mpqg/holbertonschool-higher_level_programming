#!/usr/bin/python3
"""
Base Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints the square details
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
