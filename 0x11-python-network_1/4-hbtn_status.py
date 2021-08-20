#!/usr/bin/python3
"""script"""


if __name__ == "__main__":
    """request"""
    import requests
    res = requests.get('https://intranet.hbtn.io/status')
    text = res.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
