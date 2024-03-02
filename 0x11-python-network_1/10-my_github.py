#!/usr/bin/python3
"""
This script uses the GitHub API to display the user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        user_info = response.json()
        user_id = user_info.get('id')
        print(user_id)
    except ValueError:
        print(None)
