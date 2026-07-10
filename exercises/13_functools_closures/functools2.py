# TODO: Add singledispatch registrations for int and list values.

from functools import singledispatch


@singledispatch
def describe(value: object) -> str:
    return f"object:{value}"


def test_integer_registration():
    assert describe(7) == "integer:7"


def test_list_registration():
    assert describe([1, 2, 3]) == "list with 3 items"


def test_default_implementation():
    assert describe("hello") == "object:hello"
