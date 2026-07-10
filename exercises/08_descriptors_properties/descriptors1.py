# TODO: Implement PositiveNumber using __set_name__, __get__, and __set__.
# Reject values less than or equal to zero with ValueError.


class PositiveNumber:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = name

    def __get__(self, instance: object, owner: type | None = None):
        return 0

    def __set__(self, instance: object, value: float) -> None:
        instance.__dict__[self.storage_name] = value


class Product:
    price = PositiveNumber()
    weight = PositiveNumber()

    def __init__(self, price: float, weight: float):
        self.price = price
        self.weight = weight


def test_descriptor_stores_independent_values():
    product = Product(10.5, 2.0)
    assert product.price == 10.5
    assert product.weight == 2.0


def test_descriptor_knows_attribute_name():
    assert Product.__dict__["price"].storage_name == "_price"


def test_descriptor_validates():
    error = None
    try:
        Product(0, 1)
    except ValueError as caught:
        error = caught
    assert isinstance(error, ValueError), "zero should be rejected"
