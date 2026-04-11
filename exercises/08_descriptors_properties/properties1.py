# TODO: Use `@property` to add validation to a class.
# The `Temperature` class should store temperature in Celsius internally
# but expose it via a property with validation (no below absolute zero).
# Also add a read-only `fahrenheit` property.


class Temperature:
    def __init__(self, celsius: float):
        # TODO: Use the property setter here (self.celsius = celsius),
        # not direct attribute access (self._celsius = celsius).
        self._celsius = celsius

    # TODO: Create a `celsius` property with a getter and setter.
    # The setter should raise ValueError if the value is below -273.15.

    # TODO: Create a read-only `fahrenheit` property.
    # Formula: fahrenheit = celsius * 9/5 + 32


def test_get_celsius():
    t = Temperature(25.0)
    assert t.celsius == 25.0


def test_set_celsius():
    t = Temperature(0.0)
    t.celsius = 100.0
    assert t.celsius == 100.0


def test_fahrenheit():
    t = Temperature(100.0)
    assert t.fahrenheit == 212.0
    t2 = Temperature(0.0)
    assert t2.fahrenheit == 32.0


def test_below_absolute_zero():
    try:
        Temperature(-300.0)
        assert False, "Should raise ValueError for temperature below absolute zero"
    except ValueError:
        pass


def test_set_below_absolute_zero():
    t = Temperature(0.0)
    try:
        t.celsius = -274.0
        assert False, "Should raise ValueError"
    except ValueError:
        pass


def test_fahrenheit_read_only():
    t = Temperature(0.0)
    try:
        t.fahrenheit = 100.0
        assert False, "fahrenheit should be read-only"
    except AttributeError:
        pass
