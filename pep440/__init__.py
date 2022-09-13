"""
A simple package with utils to check whether versions number match PEP 440.

https://www.python.org/dev/peps/pep-0440/


Example

>>> from pep440 import is_canonical
>>> is_canonical('4.1.0')
True

>>> is_canonical('4.2.1.beta2')  # 4.2.1b2 is correct
False

"""
__version__ = "0.1.2"
from argparse import ArgumentParser
import sys

from .core import (
    posint,
    tpl_string_re,
    string_re,
    loose440re,
    pep440re,
    is_canonical,
    assert_valid,
)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("version", nargs="?")
    parser.add_argument("--verbose", nargs="?")
    args = parser.parse_args()

    if args.version:
        c = is_canonical(args.version)
        if c:
            print("Version is canonical according to Pep 440")
        else:
            print("Version is not canonical according to Pep 440")
        sys.exit(not c)

    parser.print_help()
    sys.exit(2)
