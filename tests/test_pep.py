from pep440 import is_canonical

ok = [
        '1!2.3.4rc5.post6.dev7',
        '0.0.0rc0.post0.dev0',
    ]

not_ok = [
        '1!2.3.4.rc5.post6.dev7', # rc is not dot separated
        '0!0.0.0rc0.post0.dev0', # 0 epoch is not canonical
    ]
def test_ok():
    for version in ok:
        assert is_canonical(version)

def test_not_ok():
    for verion in not_ok:
        assert is_canonical('1!2.3.4.rc5.post6.dev7') == False

