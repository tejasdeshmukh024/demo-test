import pytest
import sys
import requests
import os
from unittest.mock import patch, MagicMock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_octocat_user(client):
    """Test octocat gists with mock data."""
    with patch('app.requests.get') as mock_get:
        # Mock successful octocat response
        mock_response = MagicMock()
        mock_response.json.return_value = [
            {
                'id': '1234567890abcdef',
                'description': 'Hello World Examples',
                'public': True,
                'html_url': 'https://gist.github.com/octocat/1234567890abcdef',
                'files': {'hello_world.rb': {'filename': 'hello_world.rb'}},
                'created_at': '2011-01-26T19:14:43Z'
            }
        ]
        mock_response.raise_for_status.return_value = None
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        response = client.get('/octocat')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user'] == 'octocat'
        assert len(data['gists']) == 1

def test_invalid_user(client):
    """Test non-existent user returns empty list (GitHub returns 200 + [])."""
    with patch('app.requests.get') as mock_get:
        # Mock empty gists response
        mock_response = MagicMock()
        mock_response.json.return_value = []  # Empty list
        mock_response.raise_for_status.return_value = None
        mock_response.status_code = 500
        mock_get.return_value = mock_response
        
        response = client.get('/nonexistentuser12345')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user'] == 'nonexistentuser12345'
        assert data['gists'] == []

def test_user_not_found(client):
    """Test that a nonexistent user returns an empty list."""
    with patch('app.requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
        mock_response.status_code = 404
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        response = client.get('/nonexistentuser12345')
        assert response.status_code == 200
        data = response.get_json()
        assert data['user'] == 'nonexistentuser12345'
        assert data['gists'] == []