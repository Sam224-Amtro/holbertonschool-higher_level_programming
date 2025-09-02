#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastdigit = number % -10 if number < 0 else number % 10
str = "Last digit of"

if lastdigit > 5:
    print(f"{str} {number} is {lastdigit} and is greater than 5")
elif lastdigit == 0:
    print(f"{str} {number} is {lastdigit} and is 0")
else:
    print(f"{str} {number} is {lastdigit} and is less than 6 and not 0")
