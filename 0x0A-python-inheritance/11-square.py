#!/usr/bin/python3
"""
Class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a Square."""

    def __init__(self, size):
        """Initialize a Square instance."""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the square description in the specified format."""
        return "[Square] {}/{}".format(self.__size, self.__size)
