#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
res1 = 'and is less than 6 and not 0'
res2 = 'and is 0'
res3 = 'and is greater than 5'
if number < 0 and (number % 10) != 0:
    print(f'Last digit of {number} is -{abs(number) % 10} {res1}')
elif (number % 10) < 6 and (number % 10) != 0:
   print(f'Last digit of {number} is {number % 10} {res1}') 
elif (number % 10) == 0:
   print(f'Last digit of {number} is 0 {res2}') 
else:
   print(f'Last digit of {number} is {number % 10} {res3}') 
