#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sw '%{size_download}\n' -o /dev/null "$1"
