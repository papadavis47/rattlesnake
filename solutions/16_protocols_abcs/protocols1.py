from typing import Protocol, runtime_checkable


@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...


@runtime_checkable
class Resizable(Protocol):
    def resize(self, factor: float) -> None: ...


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> str:
        return f"Circle(radius={self.radius})"

    def resize(self, factor: float) -> None:
        self.radius *= factor


class Text:
    def __init__(self, content: str):
        self.content = content

    def draw(self) -> str:
        return f"Text({self.content!r})"


def render(shape: Drawable) -> str:
    """Render a drawable shape."""
    return shape.draw()


def scale(obj: Resizable, factor: float) -> None:
    """Scale a resizable object."""
    obj.resize(factor)


def test_circle_is_drawable():
    c = Circle(5.0)
    assert render(c) == "Circle(radius=5.0)"


def test_text_is_drawable():
    t = Text("hello")
    assert render(t) == "Text('hello')"


def test_circle_is_resizable():
    c = Circle(5.0)
    scale(c, 2.0)
    assert c.radius == 10.0


def test_protocol_isinstance():
    assert isinstance(Circle(1), Drawable)
    assert isinstance(Text("x"), Drawable)
    assert isinstance(Circle(1), Resizable)
    assert not isinstance(Text("x"), Resizable)
