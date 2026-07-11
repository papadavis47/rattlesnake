from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: float
    y: float
    z: float = 0.0


def test_point_creation():
    p = Point(1.0, 2.0)
    assert p.x == 1.0
    assert p.y == 2.0
    assert p.z == 0.0


def test_point_frozen():
    p = Point(1.0, 2.0)
    try:
        p.x = 5.0
        raise AssertionError("Should not be able to modify a frozen dataclass")
    except AttributeError:
        pass


def test_point_equality():
    assert Point(1.0, 2.0) == Point(1.0, 2.0)
    assert Point(1.0, 2.0, 3.0) != Point(1.0, 2.0)
