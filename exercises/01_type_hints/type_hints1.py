# TODO: Add type annotations to the function parameters and return type.
# The function should take a string name and an integer age,
# and return a formatted greeting string.


def greet(name, age):
    return f"Hello, {name}! You are {age} years old."


def test_greet():
    assert greet("Alice", 30) == "Hello, Alice! You are 30 years old."
    assert greet("Bob", 25) == "Hello, Bob! You are 25 years old."


def test_greet_types():
    import inspect

    sig = inspect.signature(greet)
    params = sig.parameters
    assert params["name"].annotation is str, "name should be annotated as str"
    assert params["age"].annotation is int, "age should be annotated as int"
    assert sig.return_annotation is str, "return type should be annotated as str"
