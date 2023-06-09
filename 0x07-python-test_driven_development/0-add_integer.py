#!/usr/bin/python3
"""
Function that adds 2 integers.
a and b must be first casted to integers if they are float.
Returns an integer: the addition of a and b.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or b must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
