#!/usr/bin/python3
def uppercase(str):
    output = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upper_char = chr(ord(char) - 32)
            output += "{}".format(upper_char)
        else:
            output += "{}".format(char)
    print(output)
