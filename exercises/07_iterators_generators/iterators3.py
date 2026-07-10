# TODO: Combine chain, cycle, and islice to build a finite playlist.

from itertools import chain, cycle, islice  # noqa: F401


def playlist(intro: list[str], loop: list[str], total: int) -> list[str]:
    """Play intro once, then repeat loop until `total` songs are returned."""
    return intro[:total]


def test_chains_intro_then_cycles():
    assert playlist(["welcome"], ["a", "b"], 6) == [
        "welcome",
        "a",
        "b",
        "a",
        "b",
        "a",
    ]


def test_is_finite_and_respects_total():
    assert playlist(["one", "two"], ["again"], 1) == ["one"]
    assert playlist([], ["x", "y"], 3) == ["x", "y", "x"]
