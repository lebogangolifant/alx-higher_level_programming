#!/usr/bin/python3
"""
Class with no class or object attribute, that prevents the user from
dynamically creating new instance attributes.
"""


class LockedClass:
    """
    A class that restricts the creation of instance attributes,
    except for 'first_name'.
    """

    __slots__ = 'first_name'
