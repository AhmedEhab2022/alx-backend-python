#!/usr/bin/env python3
""" Test client functions
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """ Class to test GithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """ Test org method
        """
        url = "https://api.github.com/orgs/{}".format(input)
        mock_get_json.return_value = {"login": input}
        client = GithubOrgClient(input)
        self.assertRaises(TypeError, client.org)
        mock_get_json.assert_called_once()

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json):
        """ Test that the _public_repos_url method returns the correct value
        """
        url = "http://example.com"
        mock_get_json.return_value = {"repos_url": url}
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, url)
        mock_get_json.assert_called_once()

    @patch('client.get_json')
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """ Test that the public_repos method returns the correct value
        """
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_payload
        mock_public_repos_url.return_value = "http://example.com"
        client = GithubOrgClient("google")
        repos = client.public_repos()
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()
        self.assertEqual(repos, ["repo1", "repo2"])
        self.assertEqual(client.public_repos("test"), [])
