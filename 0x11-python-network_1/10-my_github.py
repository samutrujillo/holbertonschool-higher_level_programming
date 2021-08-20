#!/usr/bin/python3
"""
script
"""


if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv
    r = requests.get('https://api.github.com/users/{}'.format(argv[1]),
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(r.json().get('id'))
    