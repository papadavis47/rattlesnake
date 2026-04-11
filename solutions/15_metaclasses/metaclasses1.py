class Plugin:
    """Base class that automatically registers subclasses."""

    _registry: dict[str, type] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin._registry[cls.__name__] = cls

    @classmethod
    def get_plugin(cls, name: str) -> type:
        """Look up a registered plugin by name."""
        return cls._registry[name]

    @classmethod
    def list_plugins(cls) -> list[str]:
        """Return sorted list of registered plugin names."""
        return sorted(cls._registry.keys())


class JSONPlugin(Plugin):
    fmt = "json"


class XMLPlugin(Plugin):
    fmt = "xml"


class CSVPlugin(Plugin):
    fmt = "csv"


def test_plugins_registered():
    names = Plugin.list_plugins()
    assert "JSONPlugin" in names
    assert "XMLPlugin" in names
    assert "CSVPlugin" in names


def test_get_plugin():
    assert Plugin.get_plugin("JSONPlugin") is JSONPlugin
    assert Plugin.get_plugin("XMLPlugin") is XMLPlugin


def test_plugin_count():
    assert len(Plugin.list_plugins()) == 3


def test_dynamic_registration():
    class YAMLPlugin(Plugin):
        fmt = "yaml"

    assert "YAMLPlugin" in Plugin.list_plugins()
    assert Plugin.get_plugin("YAMLPlugin") is YAMLPlugin
