# TODO: Implement Car by composing an Engine and delegating start().


class Engine:
    def __init__(self, fuel: str):
        self.fuel = fuel

    def start(self) -> str:
        return f"{self.fuel} engine started"


class Car:
    def __init__(self, model: str, engine: Engine):
        self.model = model

    def start(self) -> str:
        return "TODO"


def test_car_owns_engine():
    engine = Engine("electric")
    car = Car("Roadster", engine)
    assert car.engine is engine


def test_car_delegates_to_engine():
    car = Car("Roadster", Engine("electric"))
    assert car.start() == "Roadster: electric engine started"


def test_composition_not_inheritance():
    assert not issubclass(Car, Engine)
