#!/usr/bin/env python3
"""Returns a Tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a Tuple"""
    return (k, v**2)
