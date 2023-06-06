#!/usr/bin/python3
ascii_value = 97
output = ""
while ascii_value <= 122:
    output += "{}".format(chr(ascii_value))
    ascii_value += 1

print(output)
