import os
import shutil
import tempfile


class TempDirectory:
    """A context manager that creates a temporary directory and cleans it up."""

    def __init__(self, prefix: str = "tmp_"):
        self.prefix = prefix
        self.path: str | None = None

    def __enter__(self) -> str:
        self.path = tempfile.mkdtemp(prefix=self.prefix)
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.path and os.path.exists(self.path):
            shutil.rmtree(self.path)
        return False


def test_creates_directory():
    with TempDirectory(prefix="test_") as path:
        assert os.path.isdir(path)
        assert "test_" in os.path.basename(path)


def test_cleans_up_on_exit():
    with TempDirectory() as path:
        # Create a file inside so it's a non-empty directory
        with open(os.path.join(path, "hello.txt"), "w") as f:
            f.write("hello")
        saved_path = path
    assert not os.path.exists(saved_path)


def test_cleans_up_on_exception():
    saved_path = None
    try:
        with TempDirectory() as path:
            saved_path = path
            raise ValueError("something went wrong")
    except ValueError:
        pass
    assert saved_path is not None
    assert not os.path.exists(saved_path)
