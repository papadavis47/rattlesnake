# TODO: Use structural pattern matching (match/case) to implement a command
# parser and a shape area calculator.


def handle_command(command: tuple) -> str:
    """Parse a command tuple and return a description string.

    Supported commands:
        ("quit",)                   -> "Exiting"
        ("greet", name)             -> "Hello, {name}!"
        ("move", x, y)              -> "Moving to ({x}, {y})"
        ("move", x, y, z)           -> "Moving to ({x}, {y}, {z})"
        anything else               -> "Unknown command"
    """
    # TODO: Implement using match/case
    pass


def classify_shape(shape: dict) -> float:
    """Calculate area based on a shape dictionary.

    Shapes:
        {"type": "circle", "radius": r}           -> π * r²
        {"type": "rectangle", "width": w, "height": h} -> w * h
        {"type": "triangle", "base": b, "height": h}   -> 0.5 * b * h
        anything else -> raise ValueError
    """
    # TODO: Implement using match/case on the dict
    pass


import math


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


import pytest
