#!/usr/bin/env python3
""" Test utils.access_nested_map function
"""
import unittest
from utils import access_nested_map
from typing import Any, List, Mapping, Sequence
from parameterized import parameterized


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
        """
        self.assertEqual(access_nested_map(input[0], input[1]), expected)
