from numb3rs import validate

import pytest

def test_validate():
    assert validate("1.2.3") == False

def test_validate2():
    assert validate("1000.2.3") == False

def test_validate3():
    assert validate("255.255.255.255") == True

