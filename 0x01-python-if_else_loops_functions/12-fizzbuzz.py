#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if (x % 3 == 0) and (x % 5 == 0):
            print("FizzBuzz", end=" ")
        elif x % 5 == 0:
            print("Buzz", end=" ")
        elif x % 3 == 0:
            print("Fizz", end=" ")
        elif not (x % 3 == 0 or x % 5 == 0):
            print("{:d}".format(x), end=" ")
