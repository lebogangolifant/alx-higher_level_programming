#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after each of
these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?',
    and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    print(text.strip())
