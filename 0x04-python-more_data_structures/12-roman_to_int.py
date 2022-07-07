#!/usr/bin/python3
def roman_to_int(roman_string):
    x = 0
    if not roman_string or type(roman_string) != str:
        return 0
    else:
        for i in roman_string:
            if i == 'X':
                x +=10
            elif i == 'V':
                x += 5
            elif i == 'I':
                x += 1
            elif i == 'L':
                x += 50
            elif i == 'C':
                x += 100
            elif i == 'D':
                x += 500
            elif i == 'M':
                x += 1000
    return x 
