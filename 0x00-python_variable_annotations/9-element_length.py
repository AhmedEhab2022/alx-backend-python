#!/usr/bin/env python3
"""
type-annotated function element_length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    takes a list lst of strings and returns a list of tuples,
    each tuple having a string and an integer
    """
    return [(i, len(i)) for i in lst]
