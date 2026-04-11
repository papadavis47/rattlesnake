# TODO: Implement functions using closures, `functools.partial`,
# and `functools.lru_cache`.

from functools import lru_cache, partial


def make_multiplier(factor: int):
    """Return a closure that multiplies its argument by `factor`.

    Example: double = make_multiplier(2); double(5) -> 10
    """
    # TODO: Implement using a closure
    pass


# TODO: Use `functools.partial` to create `int_from_binary` — a version of
# the built-in `int()` function that always parses base-2 strings.
# Example: int_from_binary("1010") -> 10

# int_from_binary = ???


# TODO: Implement a recursive Fibonacci function decorated with @lru_cache
# so it doesn't recompute already-seen values.
# def fib(n: int) -> int: ...


def test_make_multiplier():
    double = make_multiplier(2)
    triple = make_multiplier(3)
    assert double(5) == 10
    assert triple(5) == 15
    assert double(0) == 0


def test_int_from_binary():
    assert int_from_binary("1010") == 10
    assert int_from_binary("1111") == 15
    assert int_from_binary("0") == 0


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(30) == 832040


def test_fib_uses_cache():
    fib.cache_clear()
    fib(20)
    info = fib.cache_info()
    # With caching, we should have cache hits for recursive calls
    assert info.hits > 0
