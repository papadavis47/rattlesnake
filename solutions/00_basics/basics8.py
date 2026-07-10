programmer = {"name": "Ada", "age": 36}
programmer["language"] = "Python"


def test_programmer():
    assert programmer["name"] == "Ada"
    assert programmer["age"] == 36
    assert programmer["language"] == "Python"
    assert len(programmer) == 3
