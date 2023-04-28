#!/usr/bin/python3
""" This module fetches a url and dispplays its response """
if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen("https://alx-intranet.hbtn.io/status") as r:
        res = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode("utf-8")))
