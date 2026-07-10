fruits = ["apple", "banana"]
fruits.append("cherry")


def test_fruits():
    assert fruits == ["apple", "banana", "cherry"]
    assert fruits[0] == "apple"
