#!/usr/bin/python3
"""
Class Square that defines a square by: (based on 6-square.py)
"""


class Square:
    """This class represents a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Methods:
        area(): Calculates the area of the square.
        my_print(): Prints the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square instance.

        Args:
            size (int): The size of the square (default: 0).
            position (tuple): The position of the square (default: (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        result = ""
        if self.size == 0:
            return result
        else:
            for _ in range(self.position[1]):
                result += "\n"
            for _ in range(self.size):
                result += " " * self.position[0] + "#" * self.size + "\n"
            return result[:-1]
