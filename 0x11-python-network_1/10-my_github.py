#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    username, password = sys.argv[1], sys.argv[2]
    basic = HTTPBasicAuth(username, password)
    response = requests.get('https://api.github.com/user', auth=basic)
    print(response.json().get('id'))
