from fuel import convert
from fuel import gauge

import pytest

def test_convert():
    assert convert("1/2") == 50.0

#def test_convert2():
#    assert convert("132") == 50.0

def test_convert5():
    with pytest.raises(ValueError):
       convert("abc")

def test_convertNegFrac():
    with pytest.raises(ValueError):
       convert("-1/-8")

def test_convertNegFrac2():
    with pytest.raises(ValueError):
       convert("1/-8")

def test_convert6():
    with pytest.raises(AttributeError):
       convert(-123)

def test_convertZero():
    with pytest.raises(ZeroDivisionError):
       convert("0/0")

def test_gauge():
    assert gauge(50) == "50%"

def test_gauge1():
    assert gauge(100) == "F"

def test_gauge2():
    assert gauge(0) == "E"

def test_gauge3():
    assert gauge(1) == "E"

def test_gauge4():
    assert gauge(99) == "F"
