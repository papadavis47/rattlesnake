from contextlib import contextmanager
from io import StringIO
import sys


@contextmanager
def capture_output():
    old_stdout = sys.stdout
    buffer = StringIO()
    sys.stdout = buffer
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout


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
