"""Test Flake8EnsureASCII class."""
import os

from flake8_ensure_ascii import Flake8EnsureASCII

MOCK_FILES_PATH = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), "files"
)


def test_latin1_encoding() -> None:
    """Test latin1 python file encoding."""

    checker = Flake8EnsureASCII(
        None, os.path.join(MOCK_FILES_PATH, "latin1.py")
    )
    ret = list(checker.run())

    assert len(ret) == 0


def test_utf8_encoding() -> None:
    """Test utf8 python file encoding."""

    checker = Flake8EnsureASCII(None, os.path.join(MOCK_FILES_PATH, "utf8.py"))
    ret = list(checker.run())

    assert len(ret) > 0
    assert ret[0][0] == 5
    assert ret[0][1] == 27
    assert "ENC100" in ret[0][2]
