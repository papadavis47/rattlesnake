import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result

    return wrapper


@timer
def slow_function():
    """A deliberately slow function."""
    time.sleep(0.1)
    return "done"


def test_timer_returns_result():
    result = slow_function()
    assert result == "done"


def test_timer_preserves_name():
    assert slow_function.__name__ == "slow_function"


def test_timer_preserves_docstring():
    assert slow_function.__doc__ == "A deliberately slow function."
