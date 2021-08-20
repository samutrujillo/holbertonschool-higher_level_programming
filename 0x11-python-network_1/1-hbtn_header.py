#!/usr/bin/python3
"""
comment
"""
import urllib.request
import sys


if __name__ == '__main__':
    """request"""
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
