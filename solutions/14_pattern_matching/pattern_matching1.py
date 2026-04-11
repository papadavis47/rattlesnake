import math

import pytest


def handle_command(command: tuple) -> str:
    """Parse a command tuple and return a description string."""
    match command:
        case ("quit",):
            return "Exiting"
        case ("greet", name):
            return f"Hello, {name}!"
        case ("move", x, y):
            return f"Moving to ({x}, {y})"
        case ("move", x, y, z):
            return f"Moving to ({x}, {y}, {z})"
        case _:
            return "Unknown command"


def classify_shape(shape: dict) -> float:
    """Calculate area based on a shape dictionary."""
    match shape:
        case {"type": "circle", "radius": r}:
            return math.pi * r ** 2
        case {"type": "rectangle", "width": w, "height": h}:
            return w * h
        case {"type": "triangle", "base": b, "height": h}:
            return 0.5 * b * h
        case _:
            raise ValueError(f"Unknown shape: {shape}")


def test_command_quit():
    assert handle_command(("quit",)) == "Exiting"


def test_command_greet():
    assert handle_command(("greet", "Alice")) == "Hello, Alice!"


def test_command_move_2d():
    assert handle_command(("move", 3, 4)) == "Moving to (3, 4)"


def test_command_move_3d():
    assert handle_command(("move", 1, 2, 3)) == "Moving to (1, 2, 3)"


def test_command_unknown():
    assert handle_command(("fly",)) == "Unknown command"


def test_circle_area():
    assert classify_shape({"type": "circle", "radius": 5}) == pytest.approx(
        math.pi * 25
    )


def test_rectangle_area():
    assert classify_shape({"type": "rectangle", "width": 3, "height": 4}) == 12.0


def test_triangle_area():
    assert classify_shape({"type": "triangle", "base": 6, "height": 4}) == 12.0


def test_unknown_shape():
    try:
        classify_shape({"type": "hexagon"})
        assert False, "Should raise ValueError"
    except ValueError:
        pass
