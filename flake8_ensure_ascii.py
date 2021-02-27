"""Module to ensure that the python code files contains only ASCII chars."""

from typing import Any
from typing import Generator
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

import ast
import sys


if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


class Flake8EnsureASCII(object):
    """Flake8 plugin class to ensure ASCII encoding."""

    name = "flake8-ensure-ascii"
    version = importlib_metadata.version(name)

    def __init__(self, tree: Optional[ast.AST], filename: str) -> None:
        """Flake8 plugin instantiation."""

        self.filename = filename

    def get_lines(self) -> List[bytes]:
        """This read the `self.filename` and return a list of bytes.

        The return list contains the file data line by line.
        """

        if self.filename in ("stdin", "-", None):
            try:
                # flake8 >= v3.0
                from flake8.engine import pep8 as stdin_utils
            except ImportError:
                from flake8 import utils as stdin_utils

            return stdin_utils.stdin_get_value().splitlines(True)[:2]
        else:
            try:
                file_fd = open(self.filename, "rb")
            except Exception:
                raise

            try:
                return file_fd.readlines()
            except Exception:
                raise
            finally:
                file_fd.close()

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        """Flake8 plugin entrypoint.

        The Generator will contain: the line number, the char offset,
        the error message and the class type.
        """

        try:
            lines = self.get_lines()

            if len(lines) == 0:
                return

            for line_no, line in enumerate(lines, start=1):
                for char_no, char in enumerate(line, start=1):

                    if char < 0 or char > 127:
                        # Since some encodings take more than 1 byte
                        # We should skip to the next line on positive detection
                        yield (
                            line_no,
                            char_no,
                            "ENC100 Non ASCII encoding found",
                            type(self),
                        )
                        break
        except IOError:
            pass
