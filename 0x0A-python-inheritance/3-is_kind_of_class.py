#!/usr/bin/python3
"""No modules imported"""


def is_kind_of_class(obj, a_class):
    """Finds if obj is an instance of a_class or a class
    inherited from a_class.

    Args:
       obj: Object passed
       a_class: Class passesd

    Returns:
        True or False
    """
    return isinstance(obj, a_class)
