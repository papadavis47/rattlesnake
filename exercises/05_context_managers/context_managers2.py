# TODO: Implement a context manager using the `@contextmanager` decorator
# from contextlib. The context manager should redirect stdout to a
# StringIO buffer and yield the buffer so the caller can inspect output.

from contextlib import contextmanager
from io import StringIO
import sys


# TODO: Implement the `capture_output` context manager using @contextmanager.
# It should:
# 1. Create a StringIO buffer
# 2. Replace sys.stdout with the buffer
# 3. Yield the buffer
# 4. Restore sys.stdout in a finally block (even if an exception occurs)


def test_captures_print():
    with capture_output() as output:
        print("hello world")
    assert output.getvalue() == "hello world\n"


def test_captures_multiple_prints():
    with capture_output() as output:
        print("line 1")
        print("line 2")
    assert output.getvalue() == "line 1\nline 2\n"


def test_restores_stdout():
    original = sys.stdout
    with capture_output():
        pass
    assert sys.stdout is original


def test_restores_stdout_on_exception():
    original = sys.stdout
    try:
        with capture_output():
            raise RuntimeError("oops")
    except RuntimeError:
        pass
    assert sys.stdout is original
