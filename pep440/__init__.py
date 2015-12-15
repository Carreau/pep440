
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


__version__ = '0.0.2'

import re

posint = '(0|[1-9]\d*)'

string_re = ('^' # Start
            '([1-9]\d*!)?'        # [N!]
            '{posint}'            # N
            '(.{posint})*'        # (.N)*
            '((a|b|rc){posint})?' # [{a|b|rc}N]
            '(\.post{posint})?'  # [.postN]
            '(\.dev{posint})?'   # [.devN]
            '$'.format(posint=posint))
pep440re = re.compile(string_re)

def is_canonical(version)->bool:
    """
    Retunr wether or not the version string is canonical according to Pep 440
    """
    return pep440re.match(version) is not None

def assert_valid(version):
    if not is_canonical(version):
        raise AssertionError("Version string {!r} does not match PEP 440 specification".format(version))
        
