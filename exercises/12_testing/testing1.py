# TODO: Write pytest tests using fixtures and parametrize.
# The `Calculator` class is provided — your job is to write the tests.

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


# TODO: Create a pytest fixture called `calc` that returns a fresh Calculator instance.


# TODO: Write a test `test_add` that uses the `calc` fixture and asserts 2 + 3 == 5.


# TODO: Write a test `test_divide` that uses the `calc` fixture and asserts 10 / 4 == 2.5.


# TODO: Write a test `test_divide_by_zero` that uses the `calc` fixture
# and asserts that dividing by zero raises ZeroDivisionError.
# Use `pytest.raises(ZeroDivisionError)`.


# TODO: Write a test `test_history` that uses the `calc` fixture, performs
# two operations, and checks that calc.history has 2 entries.


# TODO: Use @pytest.mark.parametrize to write `test_add_parametrized`
# that tests multiple input/output pairs:
#   (1, 1, 2), (0, 0, 0), (-1, 1, 0), (0.1, 0.2, 0.3)
# Note: for floating point, use pytest.approx() for the last case.
