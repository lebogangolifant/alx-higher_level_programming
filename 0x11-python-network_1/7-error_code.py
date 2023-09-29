#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        response = requests.get(url)

        print(response.text)

        if response.status_code >= 400:
            print(f"Error code: {response.status_code}\n")
    else:
        print("Usage: ./7-error_code.py <URL>\n")
