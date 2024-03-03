#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


def list_commits(limit):
    """
        Lists commits on a given GitHub repository
    :param limit: number of commits to list
    """
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo_name}/commits?per_page={limit}'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            name = commit.get("commit").get("author").get("name")
            print(f'{commit.get("sha")}: {name}')
    elif response.status_code == 404:
        print("Repo/commits not found.")
    else:
        print(f"Failed to retrieve commits. Status code: {response.status_code}")


if __name__ == "__main__":
    list_commits(10)
