#!/usr/bin/env python3

for ascii_value in range(122, 96, -1):
    if ascii_value % 2 == 0:
        print("{:c}".format(ascii_value), end="")
    else:
        print("{:c}".format(ascii_value - 32), end="")

print()
