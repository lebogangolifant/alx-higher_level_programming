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

    def update(self, *args, **kwargs):
        """Update the Square instance with the given arguments"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Square instance"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
