# TODO: Define TrafficLight as an Enum whose members use auto().
# Add a `can_go` property that is true only for GREEN.

from enum import Enum, auto  # noqa: F401


class TrafficLight(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

    @property
    def can_go(self) -> bool:
        return False


def test_auto_assigns_distinct_values():
    assert len({light.value for light in TrafficLight}) == 3
    assert all(not isinstance(light.value, str) for light in TrafficLight)


def test_enum_behavior():
    assert TrafficLight.GREEN.can_go is True
    assert TrafficLight.RED.can_go is False
    assert TrafficLight.YELLOW.can_go is False
