def add(left, right):
    return left + right


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(1.5, 2.5) == 4.0
