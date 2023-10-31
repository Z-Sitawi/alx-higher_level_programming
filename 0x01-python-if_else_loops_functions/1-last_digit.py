#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    ld = number % 10
elif number < 0:
    ld = -number % 10
    ld = -ld
else:
    ld = 0

if ld > 5:
    print(f"Last digit of {number:d} is {ld:d} and is greater than 5")
elif ld == 0:
    print(f"Last digit of {number:d} is {ld:d} and is 0")
elif ld < 6 and not 0:
    print(f"Last digit of {number:d} is {ld:d} and is less than 6"
          f" and not 0")
