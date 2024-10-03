#!/usr/bin/env python3
import asyncio
import time

async def measure_runtime():
    cmp = __import__("1-async_comprehension").async_comprehension
    start = time.perf_counter()
    cmps = await asyncio.gather(cmp(), cmp(), cmp(), cmp())
    return time.perf_counter() - start

