#!/usr/bin/python3
"""
Class MyInt that inherits from int:
"""


class MyInt(int):
    """Class representing a rebel integer."""

    def __eq__(self, other):
        """Override the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator."""
        return super().__eq__(other)
