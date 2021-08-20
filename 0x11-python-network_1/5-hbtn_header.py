#!/usr/bin/python3
"""
Script
"""


if __name__ == "__main__":
    """request"""
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
