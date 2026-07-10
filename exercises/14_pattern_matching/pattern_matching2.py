# TODO: Use class patterns to describe Point and Circle dataclass instances.

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Circle:
    radius: float


def describe(shape: object) -> str:
    return "unknown"


def test_matches_origin():
    assert describe(Point(0, 0)) == "origin"


def test_matches_point_fields():
    assert describe(Point(2, 3)) == "point at 2,3"


def test_matches_circle_field():
    assert describe(Circle(2.5)) == "circle radius 2.5"
