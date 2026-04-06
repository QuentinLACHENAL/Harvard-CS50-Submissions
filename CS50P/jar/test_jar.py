from jar import Jar
import pytest


def test_init():
    jar1 = Jar(3)
    jar1.deposit(2)
    assert str(jar1) == "🍪🍪"


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    jar.withdraw(1)
    with pytest.raises(ValueError):
        jar.withdraw(3)
