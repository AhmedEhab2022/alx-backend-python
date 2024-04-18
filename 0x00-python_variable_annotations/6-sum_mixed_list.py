#!/usr/bin/env python3
"""
this module contains a function that
which takes a list mxd_lst of mixed floats and integers as argument
and returns their sum as a float.

"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of mixed floats and integers."""
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum
