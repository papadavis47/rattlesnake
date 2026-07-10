# TODO: Implement the parameterized @repeat(times) decorator.
# Call the wrapped function `times` times, return its final result,
# and preserve metadata.

from functools import wraps


def repeat(times: int):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs)

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
