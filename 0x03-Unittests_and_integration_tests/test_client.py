#!/usr/bin/env python3
""" Test client functions
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock
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
        mock_get_json.assert_called_once_with(url)
