#!/usr/bin/python3
"""
Function that returns True if the object is an instance of, or if the object
is an instance of a class that inherited:
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or, False otherwise."""
    return isinstance(obj, a_class)
