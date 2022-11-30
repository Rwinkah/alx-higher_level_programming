#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    res = 'negative'
else:
    res = 'positive'
print(f'{number} is {res}')
