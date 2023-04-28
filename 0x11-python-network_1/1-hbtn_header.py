#!/usr/bin/python3
"""
    This script sends a request to a URL and displays the value of the
    X-Request-Id variable found in the header of the response
"""
if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen

    with urlopen(argv[1]) as r:
        headers = r.info()
        print(headers["X-Request-Id"])
