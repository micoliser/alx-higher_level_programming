#!/usr/bin/python3
"""
    This script sends a POST request to a URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
"""
if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen
    from urllib.parse import urlencode

    data = urlencode({"email": argv[2]}).encode("ascii")
    with urlopen(argv[1], data) as r:
        print(r.read().decode("utf-8"))
