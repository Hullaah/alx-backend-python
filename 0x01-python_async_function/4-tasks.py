#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2 int
arguments (in this order): n and max_delay. You will
spawn wait_random n times with the specified max_delay
"""
from asyncio import as_completed
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """spawn wait_random n times with the specified max_delay"""
    delays = []
    for x in as_completed(task_wait_random(max_delay) for _ in range(n)):
        delays.append(await x)
    return delays
