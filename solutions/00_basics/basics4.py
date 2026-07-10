def describe_temperature(temperature):
    if temperature <= 0:
        return "freezing"
    elif temperature >= 30:
        return "hot"
    else:
        return "mild"


def test_describe_temperature():
    assert describe_temperature(-5) == "freezing"
    assert describe_temperature(0) == "freezing"
    assert describe_temperature(18) == "mild"
    assert describe_temperature(30) == "hot"
    assert describe_temperature(40) == "hot"
