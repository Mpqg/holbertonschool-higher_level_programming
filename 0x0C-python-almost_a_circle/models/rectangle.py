#!/usr/bin/python 3
"""Base Rectangle"""


from models.base import Base


class Rectangle(Base):
    """
    def __init__(self,width,height, x=0,y=0, id=None)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width"""
        return self.__width

    @property
    def height(self):
        """Get height"""
        return self.__height

    @property
    def x(self):
        """Get x"""
        return self.__x

    @property
    def y(self):
        """Get y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set width"""
        self.__width = value

    @height.setter
    def height(self, value):
        """Set height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """Set x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """Set y"""
        self.__y = value
