#!/usr/bin/python3
"""No modules imported"""


class LockedClass:
    """Class LockedClass"""

    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """Initialize LockedClass instance"""
        self.first_name = first_name
