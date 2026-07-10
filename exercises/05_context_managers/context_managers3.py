# TODO: Use ExitStack to enter a dynamic number of context managers.

from contextlib import AbstractContextManager
from typing import Any


def enter_all(resources: list[AbstractContextManager[Any]]) -> list[Any]:
    """Enter every resource, collect its value, then close all resources."""
    return []


class TrackedResource:
    def __init__(self, name: str, events: list[str]):
        self.name = name
        self.events = events

    def __enter__(self) -> str:
        self.events.append(f"enter {self.name}")
        return self.name

    def __exit__(self, *exc_info: object) -> None:
        self.events.append(f"exit {self.name}")


def test_dynamic_resources_close_in_reverse_order():
    events: list[str] = []
    resources = [TrackedResource(name, events) for name in ("a", "b", "c")]
    assert enter_all(resources) == ["a", "b", "c"]
    assert events == ["enter a", "enter b", "enter c", "exit c", "exit b", "exit a"]


def test_empty_resource_list():
    assert enter_all([]) == []
