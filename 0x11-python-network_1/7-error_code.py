#!/usr/bin/python3
"""
    This script sends a request to the URL and displays the body of the
    response or an error on error
"""
if __name__ == "__main__":
    import requests
    from requests.exceptions import HTTPError
    from sys import argv

    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
