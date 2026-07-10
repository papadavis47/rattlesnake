def countdown(start):
    numbers = []
    while start > 0:
        numbers.append(start)
        start -= 1
    return numbers


def test_countdown():
    assert countdown(3) == [3, 2, 1]
    assert countdown(1) == [1]
    assert countdown(0) == []
