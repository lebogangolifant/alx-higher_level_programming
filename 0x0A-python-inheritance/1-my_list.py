#!/usr/bin/python3
"""
Class MyList that inherits from list:
"""


class MyList(list):
    """Subclass list with additional print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
