#!/usr/bin/python3
output = ""
for ascii_value in range(122, 96, -1):
    if ascii_value % 2 == 0:
        output += "{:c}".format(ascii_value)
    else:
        output += "{:c}".format(ascii_value - 32)

print(output, end="")
