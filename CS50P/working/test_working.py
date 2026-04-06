from working import convert

import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == '09:00 to 17:00'


def test_convert3():
    with pytest.raises(ValueError):
        convert("aez")

