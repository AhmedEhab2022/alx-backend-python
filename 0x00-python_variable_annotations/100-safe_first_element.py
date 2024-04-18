#!/usr/bin/env python3
"""safe_first_element function"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    takes a list of any type and returns the first element
    if there is any, otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
