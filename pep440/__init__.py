
"""
A simple Package that expose utils to check wether versions number match pep440.

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

def is_valid(version):
    return pep440re.match(version) is not None

def assert_valid(version):
    if not is_valid(version):
        raise ValueError("Versions String does apparently not match Pep 440 specification")
        
