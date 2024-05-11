#!/usr/bin/env python3
""" Test utils functions
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Dict


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
    def test_get_json(self, mock_get) -> Dict:
        """ Test get_json function
        """
        mock_response1 = Mock()
        mock_response2 = Mock()
        response_dict1 = {"payload": True}
        response_dict2 = {"payload": False}
        mock_response1.json.return_value = response_dict1
        mock_response2.json.return_value = response_dict2

        url = "http://example.com"
        mock_get.return_value = mock_response1
        response = get_json(url)
        self.assertEqual(response, response_dict1)

        url = "http://holberton.io"
        mock_get.return_value = mock_response2
        response = get_json(url)
        self.assertEqual(response, response_dict2)


class TestMemoize(unittest.TestCase):
    """ Main class to test memoize function
    """
    def test_memoize(self):
        """ Test memoize function
        """
        class TestClass:
            """ Class to test memoize function
            """
            def a_method(self):
                """ Return 42
                """
                return 42

            @memoize
            def a_property(self):
                """ Call a_method function
                """
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=lambda: 42
        ) as mock_method:
            test_obj = TestClass()
            result1 = test_obj.a_property()
            result2 = test_obj.a_property()

            mock_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
