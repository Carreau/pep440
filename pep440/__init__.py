
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

from argparse import ArgumentParser

import re
import sys

__version__ = '0.0.3'


posint = '(0|[1-9]\d*)'

# 0!0.0.0rc0.post0.dev0

tpl_string_re = ('^' # Start
            '([1-9]\d*!)?'        # [N!]
            '{posint}'            # N
            '(\.{posint})*'        # (.N)*
            '((a|b|rc){posint})?' # [{a|b|rc}N]
            '(\.post{posint})?'  # [.postN]
            '(\.dev{postdev})?'   # [.devN]
            '$')
string_re = tpl_string_re.format(posint=posint, postdev=posint)
loose440re = re.compile(tpl_string_re.format(posint=posint, postdev=(posint+'?')))
pep440re = re.compile(string_re)

def is_canonical(version, loosedev=False):
    """
    Return whether or not the version string is canonical according to Pep 440
    """
    if loosedev:
        return loose440re.match(version) is not None
    return pep440re.match(version) is not None

def assert_valid(version):
    if not is_canonical(version):
        raise AssertionError("Version string {!r} does not match PEP 440 specification".format(version))


def main():
    parser = ArgumentParser()
    parser.add_argument('version', nargs='?')
    parser.add_argument('--verbose', nargs='?')
    args = parser.parse_args()

    if args.version:
        c=is_canonical(args.version)
        if c:
            print('Version is canonical according to Pep 440')
        else:
            print('Version is not canonical according to Pep 440')
        sys.exit(not c)

    parser.print_help()
    sys.exit(-1)

