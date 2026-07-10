from enum import Enum, auto


class TrafficLight(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()

    @property
    def can_go(self) -> bool:
        return self is TrafficLight.GREEN


def test_auto_assigns_distinct_values():
    assert len({light.value for light in TrafficLight}) == 3
    assert all(not isinstance(light.value, str) for light in TrafficLight)


def test_enum_behavior():
    assert TrafficLight.GREEN.can_go is True
    assert TrafficLight.RED.can_go is False
    assert TrafficLight.YELLOW.can_go is False
