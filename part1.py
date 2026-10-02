import requests
import json
import unittest

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
        repocom = (f'Repo: {repositories['name']}, Commits: {commit}')
    return repocom
getUserInfo('sostoeckel')

class TestInfo(unittest.TestCase):
     def testrepo(self):
        self.assertEqual(getUserInfo('raecelano'),('Repo: CPE-322, Commits: 5'))
     def testrepo2(self):
        self.assertEqual(getUserInfo('DOGq3'),('Repo: DOGq3, Commits: 30'))

if __name__ == '__main__':
    unittest.main()