#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lnum = ((number * -1) % 10) * -1
else:
    lnum = number % 10
if lnum > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lnum))
elif lnum == 0:
    print("Last digit of {} is {} and is 0".format(number, lnum))
elif lnum < 6 and lnum != 0:
    print("Last digit of {} is {} \
and is less than 6 and not 0".format(number, lnum))
