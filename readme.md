# PEP 440

A simple package with utils to check whether versions number match [Pep
440](https://www.python.org/dev/peps/pep-0440/)


Example:

```
>>> from pep440 import is_canonical
>>> is_canonical('4.1.0')
True

>>> is_canonical('4.2.1.beta2')  # 4.2.1b2 is correct
False
```

For a bigger dependencies with more utilities see [PyPA Packaging (version
submodule)](https://pypi.python.org/pypi/packaging)
