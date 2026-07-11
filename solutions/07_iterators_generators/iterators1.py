class Countdown:
    """An iterator that counts down from `start` to 1."""

    def __init__(self, start: int):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


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
        raise AssertionError("Should raise StopIteration")
    except StopIteration:
        pass
