#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    param = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=param)
    try:
        json_resp = response.json()
        if json_resp:
            print(f"[{json_resp['id']}] {json_resp['name']}")
        else:
            print('No result')
    except Exception:
        print("Not a valid JSON")
