#!/usr/bin/python3
""" A Python script that takes in a URL as 1st arg, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as rsp:
        print(dict(rsp.headers)['X-Request-Id'])
