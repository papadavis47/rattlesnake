class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says woof!"


def test_dog():
    dog = Dog("Riley")
    assert dog.name == "Riley"
    assert dog.speak() == "Riley says woof!"
