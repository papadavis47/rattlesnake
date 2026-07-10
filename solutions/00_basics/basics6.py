def add_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def test_add_numbers():
    assert add_numbers([1, 2, 3, 4]) == 10
    assert add_numbers([5, -2, 7]) == 10
    assert add_numbers([]) == 0
