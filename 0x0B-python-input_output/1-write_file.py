#!/usr/bin/python3
"""writes a string to a text file module"""


def write_file(filename="", text=""):
    """
       Writes a string to a text file (UTF8) and returns the number of
       characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
