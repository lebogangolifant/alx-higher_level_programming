#!/usr/bin/python3
"""Module  class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor for Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size (same as width)"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size (same as width)"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
