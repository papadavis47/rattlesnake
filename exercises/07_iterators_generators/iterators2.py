# TODO: Implement generators using `yield` and `yield from`.


def fibonacci(n: int):
    """Yield the first `n` Fibonacci numbers (starting 0, 1, 1, 2, ...)."""
    # TODO: Implement using yield
    pass


def flatten(nested: list):
    """Recursively flatten a nested list structure.

    Example: [1, [2, [3, 4]], 5] -> 1, 2, 3, 4, 5

    Use `yield from` for recursive cases.
    """
    # TODO: Implement — if an element is a list, use `yield from flatten(element)`,
    # otherwise yield the element.
    pass


def test_fibonacci_five():
    assert list(fibonacci(5)) == [0, 1, 1, 2, 3]


def test_fibonacci_one():
    assert list(fibonacci(1)) == [0]


def test_fibonacci_zero():
    assert list(fibonacci(0)) == []


def test_flatten_nested():
    assert list(flatten([1, [2, [3, 4]], 5])) == [1, 2, 3, 4, 5]


def test_flatten_already_flat():
    assert list(flatten([1, 2, 3])) == [1, 2, 3]


def test_flatten_deeply_nested():
    assert list(flatten([[[1]], [[2]], [[3]]])) == [1, 2, 3]


def test_flatten_empty():
    assert list(flatten([])) == []
