from um import count

import pytest

def test_count():
    assert count("um") == 1

def test_count2():
    assert count("um?") == 1

def test_count3():
    assert count("Um, thanks for the album.") == 1

def test_count4():
    assert count("Uuum, thanks for the album.") == 0

