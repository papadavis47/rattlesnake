# TODO: Implement a custom iterator class `Countdown` that counts down from
# a given number to 1. It must implement `__iter__` and `__next__`.


class Countdown:
    """An iterator that counts down from `start` to 1."""

    def __init__(self, start: int):
        self.start = start

    # TODO: Implement __iter__ — return self

    # TODO: Implement __next__ — return the next value in the countdown.
    # Raise StopIteration when the countdown is exhausted.


def test_countdown_list():
    assert list(Countdown(5)) == [5, 4, 3, 2, 1]


def test_countdown_zero():
    assert list(Countdown(0)) == []


def test_countdown_in_for_loop():
    result = []
    for n in Countdown(3):
        result.append(n)
    assert result == [3, 2, 1]


def test_countdown_is_iterator():
    c = Countdown(3)
    assert iter(c) is c
    assert next(c) == 3
    assert next(c) == 2
    assert next(c) == 1
    try:
        next(c)
        assert False, "Should raise StopIteration"
    except StopIteration:
        pass
