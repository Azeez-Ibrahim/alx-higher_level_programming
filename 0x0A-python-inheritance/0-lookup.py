#!/usr/bin/python3
"""No modules imported"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: Object to look into

    Returns:
        List of attributes and methods
    """

    return dir(obj)
