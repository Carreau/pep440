
"""
A simple package with utils to check whether versions number match PEP 440.

https://www.python.org/dev/peps/pep-0440/


Example

>>> from pep440 import is_valid
>>> is_valid('4.1.0')
True

>>> is_valid('4.2.1.beta2')  # 4.2.1b2 is correct
False

"""


__version__ = '0.0.1'

import re


pep440re = re.compile('^([1-9]\d*!)?'        # [N!]
                      '([1-9]\d*)'           # N
                      '(.[1-9]\d*)*'         # (.N)*
                      '((a|b|rc)[0-9]\d*)?' # [{a|b|rc}N]
                      '(\.post[1-9]\d*)?'         # [.postN]
                      '(\.dev[1-9]\d*)?$'         # [.devN]
                      )

def is_canonical(version)->bool:
    """
    Retunr wether or not the version string is canonical according to Pep 440
    """
    return pep440re.match(version) is not None

def assert_valid(version):
    if not is_canonical(version):
        raise AssertionError("Version string {!r} does not match PEP 440 specification".format(version))
        
