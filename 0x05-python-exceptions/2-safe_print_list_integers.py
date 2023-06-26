#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    num_printed = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int and num_printed != x:
                print('{:d}'.format(my_list[i]), end='')
                num_printed += 1
        except TypeError:
            continue

    print()

    return num_printed
