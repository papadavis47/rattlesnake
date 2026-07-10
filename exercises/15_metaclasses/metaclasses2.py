# TODO: Implement FieldCollector.__new__ to gather public annotated fields.


class FieldCollector(type):
    def __new__(mcls, name: str, bases: tuple[type, ...], namespace: dict):
        return super().__new__(mcls, name, bases, namespace)


class Record(metaclass=FieldCollector):
    pass


class User(Record):
    name: str
    age: int
    _internal: bool


def test_metaclass_collects_public_fields():
    assert User.fields == ("name", "age")


def test_result_is_created_by_real_metaclass():
    assert isinstance(User, FieldCollector)
