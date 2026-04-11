from __future__ import annotations


def find_user(user_id: int) -> dict | None:
    """Return user dict or None if not found."""
    users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
    return users.get(user_id)


def format_name(first: str, last: str | None = None) -> str:
    """Format a full name. Last name is optional."""
    if last is None:
        return first
    return f"{first} {last}"


def test_find_user():
    assert find_user(1) == {"name": "Alice"}
    assert find_user(99) is None


def test_format_name():
    assert format_name("Alice") == "Alice"
    assert format_name("Alice", "Smith") == "Alice Smith"
