import pytest


class Calculator:
    """A simple calculator that tracks history."""

    def __init__(self):
        self.history: list[str] = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result


@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(2, 3) == 5


def test_divide(calc):
    assert calc.divide(10, 4) == 2.5


def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)


def test_history(calc):
    calc.add(1, 2)
    calc.divide(10, 5)
    assert len(calc.history) == 2


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
        (0.1, 0.2, pytest.approx(0.3)),
    ],
)
def test_add_parametrized(calc, a, b, expected):
    assert calc.add(a, b) == expected
