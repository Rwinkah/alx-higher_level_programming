#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    pos_number = -1 * number
else:
    pos_number = number
if (pos_number % 10) < 6 and (pos_number % 10) != 0:
    res = 'and is less than 6 and not 0'
elif (pos_number % 10) == 0:
    res = 'and is 0'
else:
    res = 'and is greater than 5'

if (number > 0):
    print(f'Last digit of {number} is {number % 10} {res}')
elif (number < 0):
    print(f'Last digit of {number} is -{pos_number % 10} {res}')
else:
    print(f'Last digit of {number} is {pos_number % 10} {res}')
