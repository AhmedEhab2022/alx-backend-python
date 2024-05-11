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
        mock_response1 = Mock()
        mock_response2 = Mock()
        response_dict1 = {"payload": True}
        response_dict2 = {"payload": False}
        mock_response1.json.return_value = response_dict1
        mock_response2.json.return_value = response_dict2

        test_url = "http://example.com"
        mock_get.return_value = mock_response1
        response = get_json(test_url)
        self.assertEqual(response, response_dict1)

        test_url = "http://holberton.io"
        mock_get.return_value = mock_response2
        response = get_json(test_url)
        self.assertEqual(response, response_dict2)
