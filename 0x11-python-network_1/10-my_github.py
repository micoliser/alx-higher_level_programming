#!/usr/bin/python3
"""
    This script takes a user's GitHub credentials (username and password)
    and uses the GitHub API to display the user's id
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    headers = {
        "Authorization": "Bearer {}".format(argv[2]),
        "X-GitHub-Api-Version": "2022-11-28"
    }
    res = requests.get("https://api.github.com/user", headers=headers)
    try:
        print(res.json()["id"])
    except KeyError:
        print(None)
