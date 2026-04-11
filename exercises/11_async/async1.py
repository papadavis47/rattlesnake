# TODO: Implement async functions using `async`/`await` and `asyncio`.

import asyncio


async def fetch_data(name: str, delay: float) -> dict:
    """Simulate fetching data with a delay.

    Return a dict with "name" and "status" keys.
    """
    # TODO: Use `await asyncio.sleep(delay)` to simulate async I/O,
    # then return {"name": name, "status": "ok"}
    pass


async def fetch_all(items: list[tuple[str, float]]) -> list[dict]:
    """Fetch all items concurrently using asyncio.gather.

    Each item is a (name, delay) tuple. Return results in the same order.
    """
    # TODO: Create a list of fetch_data coroutines and use asyncio.gather
    # to run them all concurrently. Return the gathered results.
    pass


def test_fetch_single():
    result = asyncio.run(fetch_data("users", 0.01))
    assert result == {"name": "users", "status": "ok"}


def test_fetch_all_results():
    items = [("users", 0.01), ("posts", 0.01), ("comments", 0.01)]
    results = asyncio.run(fetch_all(items))
    assert len(results) == 3
    assert results[0] == {"name": "users", "status": "ok"}
    assert results[1] == {"name": "posts", "status": "ok"}
    assert results[2] == {"name": "comments", "status": "ok"}


def test_fetch_all_concurrent():
    """Verify that tasks run concurrently, not sequentially."""
    items = [("a", 0.05), ("b", 0.05), ("c", 0.05)]

    import time

    start = time.perf_counter()
    asyncio.run(fetch_all(items))
    elapsed = time.perf_counter() - start

    # If run concurrently: ~0.05s. If sequential: ~0.15s.
    assert elapsed < 0.12
