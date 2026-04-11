class Base:
    def __init__(self, **kwargs):
        self.initialized_classes: list[str] = []

    def track(self, name: str):
        self.initialized_classes.append(name)


class LoggingMixin(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logging_enabled = True
        self.track("LoggingMixin")


class Serializable(Base):
    def __init__(self, fmt: str = "json", **kwargs):
        super().__init__(**kwargs)
        self.fmt = fmt
        self.track("Serializable")


class Model(LoggingMixin, Serializable):
    def __init__(self, name: str, **kwargs):
        super().__init__(**kwargs)
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
