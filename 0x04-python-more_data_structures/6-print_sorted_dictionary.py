#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_sort = sorted(a_dictionary)
    for i in dict_sort:
        print('{}: {}'.format(i, a_dictionary[i]))
