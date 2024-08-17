#!/usr/bin/env python3
"""Annotate the below function’s parameters and return values
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Annotate the below function’s parameters and return values"""
    if lst:
        return lst[0]
    else:
        return None
