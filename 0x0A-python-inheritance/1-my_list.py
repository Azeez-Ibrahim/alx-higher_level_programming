#!/usr/bin/python3
"""No modules imported"""


class MyList(list):
    """Class MyList inherits from list"""

    def print_sorted(self):
        """Print list in ascending sort"""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
