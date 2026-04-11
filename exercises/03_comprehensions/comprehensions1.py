# TODO: Rewrite each function body using a single comprehension expression.
# Do not use explicit for loops or append().


def squares_of_evens(numbers: list[int]) -> list[int]:
    """Return squares of even numbers from the input list."""
    # TODO: Replace with a list comprehension
    result = []
    for n in numbers:
        if n % 2 == 0:
            result.append(n ** 2)
    return result


def invert_dict(d: dict[str, int]) -> dict[int, str]:
    """Swap keys and values in a dictionary."""
    # TODO: Replace with a dict comprehension
    result = {}
    for k, v in d.items():
        result[v] = k
    return result


def unique_lengths(words: list[str]) -> set[int]:
    """Return the set of unique word lengths."""
    # TODO: Replace with a set comprehension
    result = set()
    for w in words:
        result.add(len(w))
    return result


def test_squares_of_evens():
    assert squares_of_evens([1, 2, 3, 4, 5, 6]) == [4, 16, 36]
    assert squares_of_evens([]) == []


def test_invert_dict():
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_unique_lengths():
    assert unique_lengths(["hi", "hello", "hey", "ok"]) == {2, 5, 3}
