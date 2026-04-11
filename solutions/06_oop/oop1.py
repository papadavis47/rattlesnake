import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self) -> float: ...


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


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
