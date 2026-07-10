from functools import singledispatch


@singledispatch
def describe(value: object) -> str:
    return f"object:{value}"


@describe.register
def _(value: int) -> str:
    return f"integer:{value}"


@describe.register
def _(value: list) -> str:
    return f"list with {len(value)} items"


def test_integer_registration():
    assert describe(7) == "integer:7"


def test_list_registration():
    assert describe([1, 2, 3]) == "list with 3 items"


def test_default_implementation():
    assert describe("hello") == "object:hello"
