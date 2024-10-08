#!/usr/bin/env python3
"""Add type annotations to the functions
"""
from typing import TypeVar, Union, Mapping, Any
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Add type annotations to the functions"""
    if key in dct:
        return dct[key]
    else:
        return default
