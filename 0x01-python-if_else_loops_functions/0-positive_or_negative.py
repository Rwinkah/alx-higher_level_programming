#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    res = 'negative'
elif number > 0:
    res = 'positive'
else:
    res = 'zero'
print(f'{number} is {res}')
