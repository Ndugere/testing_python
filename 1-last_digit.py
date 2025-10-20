#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
digit = str(number)[len(str(number)) -1]

if int(digit) > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif int(digit) < 6:
    if int(digit) != 0:
        print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {digit} and is zero")