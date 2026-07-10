def middle(text: str) -> str:
    """Return all characters except the first and last."""
    return text[1:-1]


def every_other(items: list[int]) -> list[int]:
    """Return items at indexes 0, 2, 4, and so on."""
    return items[::2]


def reversed_copy(items: list[int]) -> list[int]:
    """Return a reversed copy using a negative step."""
    return items[::-1]


def test_string_slice():
    assert middle("python") == "ytho"


def test_list_step():
    assert every_other([0, 1, 2, 3, 4, 5]) == [0, 2, 4]


def test_negative_step():
    values = [1, 2, 3]
    assert reversed_copy(values) == [3, 2, 1]
    assert values == [1, 2, 3]
