#!/usr/bin/env python3
from typing import List

async def async_comprehension() -> List[float]:
    gen = __import__("0-async_generator").async_generator
    return [x async for x in gen()]
