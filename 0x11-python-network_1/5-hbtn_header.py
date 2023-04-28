#!/usr/bin/python3
"""
    This script sends a request to a URL and displays the value of the
    X-Request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])
    print(res.headers["X-Request-Id"])
