import pytest

from pep440 import is_canonical, assert_valid

ok = [
    "1!2.3.4rc5.post6.dev7",
    "0.0.0rc0.post0.dev0",
]

# from pep440:
ok.extend(
    [
        "1.0.dev456",
        "1.0a1",
        "1.0a2.dev456",
        "1.0a12.dev456",
        "1.0a12",
        "1.0b1.dev456",
        "1.0b2",
        "1.0b2.post345.dev456",
        "1.0b2.post345",
        "1.0rc1.dev456",
        "1.0rc1",
        "1.0",
        #     "1.0+abc.5", # Not sure if version segment is canonical
        #     "1.0+abc.7",
        #     "1.0+5",
        "1.0.post456.dev34",
        "1.0.post456",
        "1.1.dev1",
    ]
)

not_ok = [
    "1!2.3.4.rc5.post6.dev7",  # rc is not dot separated
    "0!0.0.0rc0.post0.dev0",  # 0 epoch is not canonical
]


def test_ok():
    for version in ok:
        assert is_canonical(version)
        assert_valid(version)


def test_not_ok():
    for version in not_ok:
        assert is_canonical(version) == False
        with pytest.raises(AssertionError):
            assert_valid(version)


def test_ok_loose():
    assert is_canonical("2.3.4.dev", loosedev=True) == True
