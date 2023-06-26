#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_printed = 0
    output = ""

    try:
        for index in range(x):
            output += "{}".format(my_list[index])
            num_printed += 1
    except IndexError:
        pass
    finally:
        print(output)
        return num_printed
