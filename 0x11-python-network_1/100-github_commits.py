#!/usr/bin/python3
"""
Python script uses the GitHub API
to list the 10 most recent commits, and prints them.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        owner = sys.argv[2]
        repo = sys.argv[1]

        url = f'https://api.github.com/repos/{owner}/{repo}/commits'

        try:

            response = requests.get(url)
            response.raise_for_status()

            commits = response.json()[:10]
            for commit in commits:
                sha = commit['sha']
                author_name = commit['commit']['author']['name']
                print(f"{sha}: {author_name}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    else:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
