# TODO: Annotate read_first so it preserves the value type returned by Readable.

from typing import Generic, Protocol, TypeVar, get_args, get_origin

T = TypeVar("T")
T_co = TypeVar("T_co", covariant=True)


class Readable(Protocol[T_co]):
    def read(self) -> T_co: ...


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def read(self) -> T:
        return self.value


def read_first(source: Readable[object]) -> object:
    return source.read()


def test_reads_different_types():
    assert read_first(Box(42)) == 42
    assert read_first(Box("python")) == "python"


def test_protocol_is_generic():
    assert get_origin(Readable[int]) is Readable
    assert get_args(Readable[int]) == (int,)
    assert read_first.__annotations__["source"] == Readable[T]
