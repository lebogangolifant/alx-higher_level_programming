#!/usr/bin/python3
"""Search and update module"""


def append_after(filename="", search_string="", new_string=""):
    """
     Inserts a line of text to a file, after each line containing
     a specific string
    """

    with open(filename, "r+") as file:
        lines = file.readlines()

    for index, line in enumerate(lines):
        if search_string in line:
            lines.insert(index + 1, new_string)

    with open(filename, "w") as file:
        file.writelines(lines)
