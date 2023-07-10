#!/usr/bin/python3
"""
Class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
(task based on 8-rectangle.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing a Rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description in the specified format."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
