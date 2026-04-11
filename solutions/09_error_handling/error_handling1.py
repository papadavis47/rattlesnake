class ValidationError(Exception):
    def __init__(self, message: str, field: str):
        super().__init__(message)
        self.field = field


class MissingFieldError(ValidationError):
    def __init__(self, field: str):
        super().__init__(f"Missing required field: {field}", field)


class InvalidFormatError(ValidationError):
    def __init__(self, field: str, expected_format: str):
        super().__init__(
            f"Invalid format for field '{field}', expected: {expected_format}",
            field,
        )
        self.expected_format = expected_format


def validate_user(data: dict) -> dict:
    """Validate user registration data."""
    if not data.get("name"):
        raise MissingFieldError("name")
    if not data.get("email"):
        raise MissingFieldError("email")
    if "@" not in data["email"]:
        raise InvalidFormatError("email", expected_format="user@domain.com")
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
