#!/usr/bin/python3
""" A Python script that fetches https://alx-intranet.hbtn.io/status."""


import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as rsp:
        bodyResponse = rsp.read()
        print('Body response:')
        print(f'\t- type: {type(bodyResponse)}')
        print(f'\t- content: {bodyResponse}')
        print(f'\t- utf8 content: {bodyResponse.decode("utf-8")}')
