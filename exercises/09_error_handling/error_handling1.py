# TODO: Implement custom exception classes and proper exception handling.
# Create a hierarchy of exceptions for a simple validation system.


# TODO: Define a base exception class `ValidationError` that inherits from Exception.
# It should accept a `message` and a `field` name.

# TODO: Define `MissingFieldError(ValidationError)` — for required fields that are empty.

# TODO: Define `InvalidFormatError(ValidationError)` — for fields with wrong format.
# It should additionally accept an `expected_format` parameter.


def validate_user(data: dict) -> dict:
    """Validate user registration data.

    Raises:
        MissingFieldError: If 'name' or 'email' is missing/empty.
        InvalidFormatError: If 'email' doesn't contain '@'.
    """
    # TODO: Implement validation logic:
    # 1. If 'name' is missing or empty, raise MissingFieldError
    # 2. If 'email' is missing or empty, raise MissingFieldError
    # 3. If 'email' doesn't contain '@', raise InvalidFormatError
    #    with expected_format="user@domain.com"
    # 4. Return the data if valid
    return data


def test_valid_user():
    data = {"name": "Alice", "email": "alice@example.com"}
    assert validate_user(data) == data


def test_missing_name():
    try:
        validate_user({"email": "a@b.com"})
        assert False, "Should raise MissingFieldError"
    except MissingFieldError as e:
        assert e.field == "name"


def test_missing_email():
    try:
        validate_user({"name": "Alice"})
        assert False, "Should raise MissingFieldError"
    except MissingFieldError as e:
        assert e.field == "email"


def test_invalid_email_format():
    try:
        validate_user({"name": "Alice", "email": "not-an-email"})
        assert False, "Should raise InvalidFormatError"
    except InvalidFormatError as e:
        assert e.field == "email"
        assert e.expected_format == "user@domain.com"


def test_exception_hierarchy():
    assert issubclass(MissingFieldError, ValidationError)
    assert issubclass(InvalidFormatError, ValidationError)
    assert issubclass(ValidationError, Exception)


def test_catch_all_validation_errors():
    errors_caught = 0
    for data in [{"name": ""}, {"name": "A", "email": "bad"}]:
        try:
            validate_user(data)
        except ValidationError:
            errors_caught += 1
    assert errors_caught == 2
