#!/usr/bin/env python3
"""This module contain a coroutine called measure_runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension four times in parallel using asyncio.gather,
    measure the total runtime and return it.
    """
    start: float = time.perf_counter()
    async_com = async_comprehension
    await asyncio.gather(async_com(), async_com(), async_com(), async_com())
    end: float = time.perf_counter()
    total_time: float = end - start
    return total_time
