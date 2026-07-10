# TODO: Create a dictionary for Ada with the keys "name" and "age".
# Ada's age is 36. Then add a "language" key with the value "Python".

programmer = {}


def test_programmer():
    assert programmer["name"] == "Ada"
    assert programmer["age"] == 36
    assert programmer["language"] == "Python"
    assert len(programmer) == 3
