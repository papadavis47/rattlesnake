from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def repeat(times: int):
    def decorator(function: Callable[P, R]) -> Callable[P, R]:
        @wraps(function)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            result = function(*args, **kwargs)
            for _ in range(times - 1):
                result = function(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"


def test_repeats_calls():
    calls: list[int] = []

    @repeat(4)
    def record() -> int:
        calls.append(1)
        return len(calls)

    assert record() == 4
    assert len(calls) == 4


def test_preserves_metadata():
    assert greet.__name__ == "greet"
    assert greet.__doc__ == "Return a greeting."
