#!/usr/bin/python3
"""
Script that takes in a URL
"""
if __name__ == "__main__":
    import urllib.error
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
