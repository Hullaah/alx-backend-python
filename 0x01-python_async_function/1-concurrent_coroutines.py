#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will
spawn wait_random n times with the specified max_delay
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    delays = []
    for x in asyncio.as_completed(wait_random(max_delay) for _ in range(n)):
        delays.append(await x)
    return delays
