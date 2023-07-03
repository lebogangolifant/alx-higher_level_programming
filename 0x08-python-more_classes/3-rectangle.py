#!/usr/bin/python3


class Rectangle:
    """
    The Rectangle class represents a rectangle shape.

    Attributes:
    - width (int): The width of the rectangle.
    - height (int): The height of the rectangle.

    Methods:
    - __init__(self, width=0, height=0): Initializes a rectangle instance.
    - width(self): Getter method for retrieving the width.
    - width(self, value): Setter method for setting the width.
    - height(self): Getter method for retrieving the height.
    - height(self, value): Setter method for setting the height.
    - area(self): Calculates and returns the rectangle area.
    - perimeter(self): Calculates and returns the rectangle perimeter.
    - __str__(self): Returns a string representation of the rectangle.
    - __repr__(self): Returns a string representation of the rectangle
    for debugging purposes.

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

    def area(self):
        """Calculates and returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
