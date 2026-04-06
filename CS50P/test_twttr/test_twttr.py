import pytest

from twttr import shorten

def test_voyelle():
    assert shorten("aeiou") == ""

def test_empty():
    assert shorten("") == ""

def test_number():
    assert shorten("12345") == "12345"

def test_uppercaseVowel():
    assert shorten("AEIOUp") == "p"

def test_punct():
    assert shorten(".?,") == ".?,"

def test_uppercased():
    assert shorten("SALUT") == "SLT"
