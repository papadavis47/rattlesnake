# TODO: Handle ValueError and TypeError subgroups separately with except*.

import builtins


def grouped_messages() -> tuple[list[str], list[str]]:
    value_errors: list[str] = []
    type_errors: list[str] = []
    try:
        raise builtins.ExceptionGroup(
            "invalid inputs", [ValueError("age"), TypeError("name")]
        )
    except* (ValueError, TypeError) as group:
        value_errors.extend(str(error) for error in group.exceptions)
    return value_errors, type_errors


def test_handles_each_exception_type():
    assert grouped_messages() == (["age"], ["name"])
