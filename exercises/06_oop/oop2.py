# TODO: Fix the diamond inheritance problem using `super()`.
# The `LoggingMixin` and `Serializable` both provide an `init` chain.
# Use cooperative multiple inheritance so all `__init__` methods
# are called correctly via `super()`.


class Base:
    def __init__(self, **kwargs):
        self.initialized_classes: list[str] = []

    def track(self, name: str):
        self.initialized_classes.append(name)


class LoggingMixin(Base):
    # TODO: Fix __init__ to use super() and pass **kwargs along the MRO chain
    def __init__(self, **kwargs):
        self.logging_enabled = True
        self.track("LoggingMixin")


class Serializable(Base):
    # TODO: Fix __init__ to use super() and pass **kwargs along the MRO chain
    def __init__(self, fmt: str = "json", **kwargs):
        self.fmt = fmt
        self.track("Serializable")


class Model(LoggingMixin, Serializable):
    # TODO: Fix __init__ to use super() and pass **kwargs along the MRO chain
    def __init__(self, name: str, **kwargs):
        self.name = name
        self.track("Model")


def test_all_inits_called():
    m = Model(name="test", fmt="xml")
    assert "Model" in m.initialized_classes
    assert "LoggingMixin" in m.initialized_classes
    assert "Serializable" in m.initialized_classes


def test_attributes_set():
    m = Model(name="test", fmt="xml")
    assert m.name == "test"
    assert m.logging_enabled is True
    assert m.fmt == "xml"


def test_mro_order():
    # Python's MRO for Model is: Model -> LoggingMixin -> Serializable -> Base
    assert Model.__mro__ == (Model, LoggingMixin, Serializable, Base, object)
