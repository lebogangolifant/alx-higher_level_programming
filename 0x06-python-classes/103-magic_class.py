#!/usr/bin/python3
"""
Python class MagicClass: (python_bytecode)
"""
import math


class MagicClass:
    """This class represents a magic circle.

    Attributes:
        radius (number): The radius of the magic circle.

    Methods:
        area(): Calculates the area of the magic circle.
        circumference(): Calculates the circumference of the magic circle.
    """

    def __init__(self, radius=0):
        """Initialize a magic circle instance.

        Args:
            radius (number): The radius of the magic circle (default: 0).

        Raises:
            TypeError: If the radius is not a number.
        """
        if type(radius) not in [int, float]:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of the magic circle.

        Returns:
            The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the magic circle.

        Returns:
            The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
