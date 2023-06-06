#!/usr/bin/python3
numbers = []
for number in range(100):
    numbers.append("{:02d}".format(number))
output = ", ".join(numbers)
print(output)
