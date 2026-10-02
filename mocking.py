from unittest.mock import Mock
from unittest.mock import patch
import json
import requests

@patch("github_api.requests.get")
def test_no_repositories(mock_get):
    response = Mock()
    response.text = json.dumps([])
    mock_get.return_value = response

    result = repositories("raecelano")

    assert result == []