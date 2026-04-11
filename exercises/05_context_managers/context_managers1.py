# TODO: Implement a context manager class called `TempDirectory` that creates
# a temporary directory on enter and removes it on exit.
# You need to implement the `__enter__` and `__exit__` methods.

import os
import tempfile
import shutil


class TempDirectory:
    """A context manager that creates a temporary directory and cleans it up."""

    def __init__(self, prefix: str = "tmp_"):
        self.prefix = prefix
        self.path: str | None = None

    # TODO: Implement __enter__ — create a temp directory using
    # tempfile.mkdtemp(prefix=self.prefix) and return its path.

    # TODO: Implement __exit__ — remove the directory tree using
    # shutil.rmtree(). It should not re-raise exceptions.


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
