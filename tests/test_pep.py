from pep440 import is_canonical


def test_ok():
    assert is_canonical('1!2.3.4rc5.post6.dev7')

def test_not_ok():
    assert is_canonical('1!2.3.4.rc5.post6.dev7') == False

