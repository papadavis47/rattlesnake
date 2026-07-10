# TODO: Implement count_up as an asynchronous generator and consume it with async for.

import asyncio
from collections.abc import AsyncIterator


async def count_up(limit: int) -> AsyncIterator[int]:
    if False:
        yield limit


async def collect(limit: int) -> list[int]:
    return []


def test_async_generator_values():
    assert asyncio.run(collect(4)) == [0, 1, 2, 3]


def test_empty_async_generator():
    assert asyncio.run(collect(0)) == []
