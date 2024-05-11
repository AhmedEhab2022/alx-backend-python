#!/usr/bin/env python3
""" Test utils.access_nested_map function
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ Class to Test access_nested_map function
    """
    @parameterized.expand([
        ([{"a": {"b": {"c": 1}}}, ["a", "b", "c"]], 1),
        ([{"a": {"b": 2}}, ("a",)], {"b": 2}),
        ([{"a": {"b": 2}}, ("a", "b")], 2),
    ])
    def test_access_nested_map(self, input, expected):
        """ Test access_nested_map function
            with normal use
        """
        self.assertEqual(access_nested_map(input[0], input[1]), expected)

    @parameterized.expand([
        ([{}, ("a",)], KeyError('a')),
        ([{"a": 1}, ("a", "b")], KeyError('b'))
    ])
    def test_access_nested_map_exception(self, input, expected):
        """ Test access_nested_map function
            with exception
        """
        self.assertRaises(
            expected.__class__, access_nested_map, input[0], input[1]
        )


class TestGetJson(unittest.TestCase):
    """ Class to test get_json function
    """
    @patch('requests.get')
    def test_get_json(self, mock_get):
        """ Test get_json function
        """
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for test_url, test_payload in test_cases:
            # Create a Mock object for the get method
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function under test
            result = get_json(test_url)

            # Assert that requests.get was called exactly once
            # with the correct URL
            mock_get.assert_called_with(test_url)

            # Assert that the result matches the expected payload
            self.assertEqual(result, test_payload)
