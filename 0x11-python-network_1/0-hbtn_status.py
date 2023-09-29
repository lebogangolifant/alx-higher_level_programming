#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using the urllib package.
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:

        body = response.read()

        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")
