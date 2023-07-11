#!/usr/bin/python3
"""Adds all arguments to a Python list"""
import json
import sys
from os import path


def add_to_list_and_save(args):
    """Adds all arguments to Python list, and then save them to a JSON file"""
    filename = 'add_item.json'

    if path.exists(filename):
        with open(filename, 'r') as file:
            my_list = json.load(file)
    else:
        my_list = []

    my_list.extend(args)

    with open(filename, 'w') as file:
        json.dump(my_list, file)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    add_to_list_and_save(arguments)
