#!/usr/bin/env python3
"""
this module contain function that
takes a string k and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v and
should be annotated as a float.

"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    type-annotated function that takes a string k and int or float v
    as arguments and returns a tuple from k and square of v
    """
    return (k, v * v)
