#!/usr/bin/env python3
''' Module: simple async generator '''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator coroutine that yields 10 random
    floating-point numbers between 0 and 10,
    with a delay of 1 second between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
