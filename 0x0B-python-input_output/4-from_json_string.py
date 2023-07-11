#!/usr/bin/python3
"""Python data structure represented by a JSON string module"""
import json


def from_json_string(my_str):
    """Returns an object Python data structure represented by a JSON string"""
    return json.loads(my_str)
