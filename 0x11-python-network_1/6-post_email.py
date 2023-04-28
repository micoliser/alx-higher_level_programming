#!/usr/bin/python3
"""
    This script sends a POST request to a URL with the email as a parameter,
    and displays the body of the response
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.post(argv[1], data={"email": argv[2]})
    print(res.text)
