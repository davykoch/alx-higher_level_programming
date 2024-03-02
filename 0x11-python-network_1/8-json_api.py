#!/usr/bin/python3
"""This script sends a POST request with a letter
as a parameter and displays the result."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}

    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
