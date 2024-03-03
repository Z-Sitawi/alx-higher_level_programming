#!/usr/bin/python3
""" A Python script that takes in a URL as 1st arg, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
from sys import argv


if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as rsp:
        print(dict(rsp.headers)['X-Request-Id'])
