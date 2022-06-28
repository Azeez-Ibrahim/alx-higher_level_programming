#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lnum = (number % 10) * -1
else :
    lnum = number % 10
if lnum > 5:
    a = "and is greater than 5"
elif lnum == 0:
    a = "and is 0"
elif lnum < 6 and lnum != 0:
    a = "and is less than 6 and not 0" 
print("Last digit of {} is {} {} ".format(number,lnum,a))
