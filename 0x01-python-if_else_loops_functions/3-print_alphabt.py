#!/usr/bin/python3
output = ''
for ascii_value in range(ord('a'), ord('z') + 1):
    if chr(ascii_value) not in {'q', 'e'}:
        output += "{}".format(chr(ascii_value))
print(output)
