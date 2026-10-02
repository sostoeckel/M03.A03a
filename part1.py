import requests
import json
import unittest
from unittest.mock import Mock
from unittest.mock import patch

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
    @patch("requests.get")
    def test_repo(self, mock_get):
        response = Mock()
        response.text = json.dumps([])
        mock_get.return_value = response
        mock_get.side_effect = [Mock(json=Mock(return_value=[{'name': 'CPE-322'}])),Mock(json=Mock(return_value=[
                {'test': '1'},
                {'test': '2'},
                {'test': '3'}
            ]))
        ]
        result = getUserInfo("raecelano")
        self.assertEqual(result,("Repo: CPE-322, Commits: 3"))
        self.assertEqual(mock_get.call_count, 2)
if __name__ == '__main__':
    unittest.main()