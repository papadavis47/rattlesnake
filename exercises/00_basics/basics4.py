# TODO: Complete the function with `if`, `elif`, and `else`.
# Return "freezing" at 0°C or below, "hot" at 30°C or above,
# and "mild" for temperatures in between.


def describe_temperature(temperature):
    return "TODO"


def test_describe_temperature():
    assert describe_temperature(-5) == "freezing"
    assert describe_temperature(0) == "freezing"
    assert describe_temperature(18) == "mild"
    assert describe_temperature(30) == "hot"
    assert describe_temperature(40) == "hot"
