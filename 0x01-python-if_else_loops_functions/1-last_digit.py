#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
message = f"Last digit of {number:d} is {last_digit:d} and is "
if last_digit > 5:
    message += "greater than 5"
elif last_digit == 0:
    message += "0"
else:
    message += "less than 6 and not 0"
print(message)