#!/usr/bin/env python3
"""This module contain measure_time function"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    Your function should return a float.
    """
    s: float = time.perf_counter()
    await wait_n(n, max_delay)
    total_time: float = time.perf_counter() - s
    return float(total_time / n)
