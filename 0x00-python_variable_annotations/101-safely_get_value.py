#!/usr/bin/env python3
""" safely_get_value function """
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')
union1 = Union[T, None]
union2 = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: union1 = None) -> union2:
    """ safely get value from dictionary """
    if key in dct:
        return dct[key]
    else:
        return default
