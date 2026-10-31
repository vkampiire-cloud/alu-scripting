#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.

    If not a valid subreddit, prints None.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])
            for child in children:
                print(child.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
