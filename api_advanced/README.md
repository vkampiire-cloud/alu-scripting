# API Advanced

This project covers querying RESTful APIs (using the Reddit API), handling pagination, parsing JSON responses, building recursive API calls, and sorting formatted data in Python.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- First line of all files must be exactly `#!/usr/bin/python3`
- All files end with a newline
- Code adheres to PEP 8 style guide (`pycodestyle`)
- Imports organized in alphabetical order
- All modules and functions have documentation (`__doc__`)
- Code must not execute when imported (`if __name__ == '__main__':`)
- All files must be executable (`chmod +x`)

## Tasks

| File | Description |
| --- | --- |
| `0-subs.py` | Function that queries the Reddit API and returns the number of subscribers for a given subreddit. |
| `1-top_ten.py` | Function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit. |
| `2-recurse.py` | Recursive function that queries the Reddit API and returns a list containing titles of all hot articles for a given subreddit. |
| `3-count.py` | Recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords. |
