#!/usr/bin/python3
"""No modules imported"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class

    Args:
       obj: Object passed
       a_class: Class passed

    Return:
       returns True or Flase
    """
    return type(obj) == a_class
