#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    The Rectangle class represents a rectangle shape.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.

    Methods:
    - __init__(self, width=0, height=0):
      Initializes a rectangle instance with optional width and height.
    - width(self): Getter method for retrieving the width.
    - width(self, value): Setter method for setting the width.
    - height(self): Getter method for retrieving the height.
    - height(self, value): Setter method for setting the height.

    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance with optional width and height.

        Args:
        - width (int): The width of the rectangle. Default is 0.
        - height (int): The height of the rectangle. Default is 0.

        """
        self.__width = 0
        self.width = width
        self.__height = 0
        self.height = height

    @property
    def width(self):
        """Getter method for retrieving the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for setting the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for retrieving the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for setting the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
