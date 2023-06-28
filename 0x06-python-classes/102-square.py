#!/usr/bin/python3
"""
Class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """This class represents a square.

    Attributes:
        size (number): The size of the square.

    Methods:
        area(): Calculates the area of the square.
        __eq__(other): Checks if the square is equal to another square.
        __ne__(other): Checks if the square is not equal to another square.
        __gt__(other): Checks if the square is greater than another square.
        __ge__(other): Checks if the square is greater than equal to another
                       square.
        __lt__(other): Checks if the square is less than another square.
        __le__(other): Checks if the square is less than or equal to another
                       square.
    """

    def __init__(self, size=0):
        """Initialize a square instance.

        Args:
            size (number): The size of the square (default: 0).
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (number): The size value to be set.

        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
