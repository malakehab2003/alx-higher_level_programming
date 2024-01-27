#!/usr/bin/python3
""" take repo name and the owner name and print commits"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    api_url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

    try:
        response = requests.get(api_url)
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except Exception as e:
        print(f"Error: {e}")

