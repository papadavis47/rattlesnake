# TODO: Replace the result below with one nested list comprehension.


def positive_values(rows: list[list[int]]) -> list[int]:
    """Flatten rows while keeping only positive values."""
    return []


def test_flattens_in_order():
    assert positive_values([[1, -2, 3], [], [-4, 5]]) == [1, 3, 5]


def test_filters_zero_and_negatives():
    assert positive_values([[0, -1], [2, 0]]) == [2]
