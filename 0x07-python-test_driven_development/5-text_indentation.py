#!/usr/bin/python3
"""
text_indentation - prints a text with 2 new lines
after each of these characters: ., ? and :
text must be a string
There should be no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()

    for char in text:
        print(char, end="")
        if char in ".?:":
            print("\n")
