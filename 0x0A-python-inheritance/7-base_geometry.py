#!/usr/bin/python3
"""
Class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """Empty class representing Base Geometry."""

    def area(self):
        """Raises an exception with the message 'area() is not implemented'."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value argument."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
