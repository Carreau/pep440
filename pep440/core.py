# This fiel is part of the python package pep 440
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

posint = "(0|[1-9]\d*)"

# 0!0.0.0rc0.post0.dev0

tpl_string_re = (
    "^"  # Start
    "([1-9]\d*!)?"  # [N!]
    "{posint}"  # N
    "(\.{posint})*"  # (.N)*
    "((a|b|rc){posint})?"  # [{a|b|rc}N]
    "(\.post{posint})?"  # [.postN]
    "(\.dev{postdev})?"  # [.devN]
    "$"
)
string_re = tpl_string_re.format(posint=posint, postdev=posint)
loose440re = re.compile(tpl_string_re.format(posint=posint, postdev=(posint + "?")))
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
        raise AssertionError(
            "Version string {!r} does not match PEP 440 specification".format(version)
        )
