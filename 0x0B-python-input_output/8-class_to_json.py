#!/usr/bin/python3
"""Class to JSON module"""


def class_to_json(obj):
    """Returns the dictionary description with a simple data structure
       for JSON serialization.
    """
    return obj.__dict__
