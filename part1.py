import requests
import json

def getUserInfo(username):
    repos = requests.get(f'https://api.github.com/users/{username}/repos')
    r = repos.json()
    for repositories in r:
        c = f'https://api.github.com/repos/{username}/{repositories['name']}/commits'
        request = requests.get(c)
        out = request.json()
        commit = 0
        for commits in out:
                commit += 1
        print(f'Repos: {repositories['name']}, Commits: {commit}')
getUserInfo('sostoeckel')