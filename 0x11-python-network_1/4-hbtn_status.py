#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using the requests package and displays the body of the response
"""

import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    if response.status_code == 200:
        body = response.text
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
    else:
        print(f"Error: {response.status_code}")
