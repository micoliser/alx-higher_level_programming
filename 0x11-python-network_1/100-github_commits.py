#!/usr/bin/python3
"""
    This script makes a request to the github api and list the 10 most
    recent commits of a repository by a user
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1])
    res = requests.get(url)

    count = 0
    for commit_dict in res.json():
        if count == 10:
            break
        sha = commit_dict["sha"]
        author = commit_dict["commit"]["author"]["name"]
        print(f"{sha}: {author}")
        count += 1
