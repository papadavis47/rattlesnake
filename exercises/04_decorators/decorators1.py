# TODO: Create a decorator called `timer` that prints how long a function
# takes to execute. Use `time.perf_counter()` for timing.
# The decorator should preserve the original function's name and docstring.

import time
from functools import wraps


# TODO: Implement the timer decorator here


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
