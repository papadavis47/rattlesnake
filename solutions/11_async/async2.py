import asyncio
from collections.abc import AsyncIterator


async def count_up(limit: int) -> AsyncIterator[int]:
    for number in range(limit):
        await asyncio.sleep(0)
        yield number


async def collect(limit: int) -> list[int]:
    values: list[int] = []
    async for number in count_up(limit):
        values.append(number)
    return values


def test_async_generator_values():
    assert asyncio.run(collect(4)) == [0, 1, 2, 3]


def test_empty_async_generator():
    assert asyncio.run(collect(0)) == []
