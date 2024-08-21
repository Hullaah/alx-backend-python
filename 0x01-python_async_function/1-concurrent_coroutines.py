#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will
spawn wait_random n times with the specified max_delay
"""
import asyncio
from typing import Coroutine, Any
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """spawn wait_random n times with the specified max_delay"""
    queue = asyncio.Queue(1)
    delays = []

    async def wait(coro: Coroutine[Any, Any, float], queue: asyncio.Queue):
        await queue.put(coro)

    for x in range(n):
        await wait(wait_random(max_delay), queue)

    for x in range(n):
        delays.append(await queue.get())
    return delays
