#!/usr/bin/python3
"""
    This script sends a request to the URL and displays the body of the response
    (decoded in utf-8) or an error on error
"""
if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen
    from urllib.error import HTTPError

    try:
        with urlopen(argv[1]) as r:
            print(r.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
