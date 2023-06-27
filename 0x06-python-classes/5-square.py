#!/usr/bin/python3
"""
class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a Square instance.
        area(self): Calculates and returns the area of the square.
        size(self): Getter method to retrieve the size attribute value.
        size(self, value): Setter method to set the size attribute value.
        my_print(self): Prints the square using "#" character.

    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute value.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute value.

        Args:
            value (int): The size value to be set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints the square using "#" character.

        If size is 0, prints an empty line.

        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
