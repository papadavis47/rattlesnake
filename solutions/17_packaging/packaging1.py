import tomllib

PYPROJECT = b"""
[project]
name = "rattlesnake-demo"
version = "1.2.0"
requires-python = ">=3.12"
dependencies = ["httpx>=0.27", "rich>=13"]
"""


def project_metadata(source: bytes) -> dict[str, object]:
    return tomllib.loads(source.decode())["project"]


def test_reads_project_identity():
    metadata = project_metadata(PYPROJECT)
    assert metadata["name"] == "rattlesnake-demo"
    assert metadata["version"] == "1.2.0"


def test_reads_python_and_dependencies():
    metadata = project_metadata(PYPROJECT)
    assert metadata["requires-python"] == ">=3.12"
    assert metadata["dependencies"] == ["httpx>=0.27", "rich>=13"]
