from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def apply_twice(operation: Callable[[int], int], value: int) -> int:
    return operation(operation(value))


def first(items: list[T]) -> T:
    return items[0]


def test_callable_annotation():
    assert apply_twice(lambda number: number + 3, 4) == 10
    assert apply_twice.__annotations__["operation"] == Callable[[int], int]


def test_generic_first():
    assert first([1, 2]) == 1
    assert first(["alpha", "beta"]) == "alpha"
    assert first.__annotations__["return"] is T
