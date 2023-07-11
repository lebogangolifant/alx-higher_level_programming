#!/usr/bin/python3
"""Appends a string module"""


def append_write(filename="", text=""):
    """
       Appends a string to a text file (UTF8) and returns the number
       of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_added = file.write(text)
    return characters_added
