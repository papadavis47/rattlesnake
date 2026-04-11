from functools import lru_cache, partial


def make_multiplier(factor: int):
    """Return a closure that multiplies its argument by `factor`."""

    def multiplier(x):
        return x * factor

    return multiplier


int_from_binary = partial(int, base=2)


@lru_cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


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
    assert info.hits > 0
