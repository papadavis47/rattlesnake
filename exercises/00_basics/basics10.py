# TODO: Finish the `Dog` class.
# Store `name` in the constructor, then make `speak` return
# "<name> says woof!" using an f-string.


class Dog:
    def __init__(self, name):
        pass

    def speak(self):
        return "TODO"


def test_dog():
    dog = Dog("Riley")
    assert dog.name == "Riley"
    assert dog.speak() == "Riley says woof!"
