#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]

        data = {'email': email}
        data = urllib.parse.urlencode(data).encode('utf-8')

        req = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    else:
        print("Usage: ./2-post_email.py <URL> <email>")
