from concurrent.futures import ThreadPoolExecutor
import time


def slow_square(n: int) -> int:
    """Simulate a slow computation."""
    time.sleep(0.05)
    return n * n


def compute_squares_sequential(numbers: list[int]) -> list[int]:
    """Compute squares sequentially (provided for comparison)."""
    return [slow_square(n) for n in numbers]


def compute_squares_concurrent(numbers: list[int]) -> list[int]:
    """Compute squares concurrently using ThreadPoolExecutor."""
    with ThreadPoolExecutor() as executor:
        return list(executor.map(slow_square, numbers))


def test_correct_results():
    numbers = [1, 2, 3, 4, 5]
    assert compute_squares_concurrent(numbers) == [1, 4, 9, 16, 25]


def test_faster_than_sequential():
    numbers = list(range(10))
    start = time.perf_counter()
    compute_squares_concurrent(numbers)
    concurrent_time = time.perf_counter() - start

    start = time.perf_counter()
    compute_squares_sequential(numbers)
    sequential_time = time.perf_counter() - start

    assert concurrent_time < sequential_time * 0.6


def test_empty_input():
    assert compute_squares_concurrent([]) == []
