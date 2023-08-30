# This file is part of the python package ``pep440``
# Feel free to vendor just this file, if should contain all you need.
#
#  Vendored version of commit <put the commit here>
#
###############################################################################
# The MIT License (MIT)
#
# Copyright (c) 2015-present  Matthias Bussonnier
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###############################################################################
import re
import string

posint = r"(0|[1-9]\d*)"

# 0!0.0.0rc0.post0.dev0
# pep440 also allow ...+<anythings a-zA-Z0-9.>, see later

tpl_string_re = (
    r"^"  # Start
    r"([1-9]\d*!)?"  # [N!]
    r"{posint}"  # N
    r"(\.{posint})*"  # (.N)*
    r"((a|b|rc){posint})?"  # [{a|b|rc}N]
    r"(\.post{posint})?"  # [.postN]
    r"(\.dev{postdev})?"  # [.devN]
    r"$"
)
string_re = tpl_string_re.format(posint=posint, postdev=posint)
loose440re = re.compile(tpl_string_re.format(posint=posint, postdev=(posint + "?")))
pep440re = re.compile(string_re)
_VALID_SET = set(string.ascii_letters + string.digits + ".")


def is_canonical(
    version: str, loosedev: bool = False, *, check_local: bool = True
) -> bool:
    """
    Return whether or not the version string is canonical according to Pep 440

    Parameters
    ----------
    version : str
        Version string to check
    loosedev : bool, optional
        Whether or not to accept non-PEP440 dev versions with `.dev` without
        number suffixes. Pep440 requires a number suffix for `.devX` versions.
        but many versions in the wild do not follow this convention.
    check_local : bool, optional
        pep440 allows for a local version identifier, which is a string of
        letters, numbers, and periods, separated from as single +.
        Check it by default. If false, assume anything after the + is valid.
    """
    cversion, plus, local = version.partition("+")
    if check_local:
        if plus == "+" and not local:
            return False
        local_correct = set(local) <= _VALID_SET
    else:
        local_correct = True
    if loosedev:
        return loose440re.match(cversion) is not None and local_correct
    return pep440re.match(cversion) is not None and local_correct


def assert_valid(version: str) -> None:
    if not is_canonical(version):
        raise AssertionError(
            "Version string {!r} does not match PEP 440 specification".format(version)
        )
