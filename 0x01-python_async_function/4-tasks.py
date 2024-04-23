#!/usr/bin/env python3
"""This module contain function task_wait_n"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in 2 int arguments (in this order): n and max_delay.
    You will spawn task_wait_random n times with the specified max_delay.
    task_wait_n should return the list of all the delays.
    The list of the delays should be in ascending order
    without using sort() because of concurrency.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)
    return delays
