from typing import Any


class PositiveNumber:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: object, owner: type | None = None):
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __set__(self, instance: object, value: float) -> None:
        if value <= 0:
            raise ValueError("value must be positive")
        setattr(instance, self.storage_name, value)


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
    descriptor: Any = Product.__dict__["price"]
    assert descriptor.storage_name == "_price"


def test_descriptor_validates():
    error = None
    try:
        Product(0, 1)
    except ValueError as caught:
        error = caught
    assert isinstance(error, ValueError), "zero should be rejected"
