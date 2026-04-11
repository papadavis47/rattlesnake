# TODO: Convert this class to a dataclass.
# Use the @dataclass decorator and remove the __init__ and __repr__ methods.
# The dataclass should be frozen (immutable).

# TODO: Add the import for dataclass


class Point:
    def __init__(self, x: float, y: float, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.z == other.z


def test_point_creation():
    p = Point(1.0, 2.0)
    assert p.x == 1.0
    assert p.y == 2.0
    assert p.z == 0.0


def test_point_frozen():
    p = Point(1.0, 2.0)
    try:
        p.x = 5.0
        assert False, "Should not be able to modify a frozen dataclass"
    except AttributeError:
        pass


def test_point_equality():
    assert Point(1.0, 2.0) == Point(1.0, 2.0)
    assert Point(1.0, 2.0, 3.0) != Point(1.0, 2.0)
