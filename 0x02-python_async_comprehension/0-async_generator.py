#!/usr/bin/env python3
import asyncio
import random
import typing

async def async_generator() -> typing.AsyncGenerator[float, None]:
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)

