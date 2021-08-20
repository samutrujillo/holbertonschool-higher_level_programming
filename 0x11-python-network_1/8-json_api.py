#!/usr/bin/python3
"""
Script
"""


if __name__ == "__main__":
    """request"""
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_dict = res.json()
        id = r_dict.get('id')
        name = r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except Exception:
        print("Not a valid JSON")
