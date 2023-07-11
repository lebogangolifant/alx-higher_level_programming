#!/usr/bin/python3
"""Object from a “JSON file” module"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
