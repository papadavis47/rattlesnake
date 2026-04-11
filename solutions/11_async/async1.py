import asyncio


async def fetch_data(name: str, delay: float) -> dict:
    """Simulate fetching data with a delay."""
    await asyncio.sleep(delay)
    return {"name": name, "status": "ok"}


async def fetch_all(items: list[tuple[str, float]]) -> list[dict]:
    """Fetch all items concurrently using asyncio.gather."""
    tasks = [fetch_data(name, delay) for name, delay in items]
    return list(await asyncio.gather(*tasks))


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

    assert elapsed < 0.12
