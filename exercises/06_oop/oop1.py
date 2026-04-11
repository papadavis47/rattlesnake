# TODO: Fix the class hierarchy. The `Shape` class should be an abstract base
# class (ABC) with an abstract method `area()`. Then implement `Circle` and
# `Rectangle` as concrete subclasses.

# TODO: Import ABC and abstractmethod from the abc module


class Shape:
    """Abstract base class for shapes."""

    # TODO: Make this class inherit from ABC and make `area` an abstract method.
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    # TODO: Implement `area` — return π * radius²
    # Use `math.pi` (you'll need to import math)


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    # TODO: Implement `area` — return width * height


import math


def test_circle_area():
    c = Circle(5.0)
    assert abs(c.area() - 78.53981633974483) < 1e-9


def test_rectangle_area():
    r = Rectangle(3.0, 4.0)
    assert r.area() == 12.0


def test_cannot_instantiate_shape():
    try:
        Shape()
        assert False, "Should not be able to instantiate an abstract class"
    except TypeError:
        pass


def test_isinstance():
    c = Circle(1.0)
    r = Rectangle(1.0, 1.0)
    assert isinstance(c, Shape)
    assert isinstance(r, Shape)
