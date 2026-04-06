from plates import is_valid

def test_toolong():
    assert is_valid("dddddddddddddd") == 0

def test_tooshort():
    assert is_valid("d") == 0

def test_numsonly():
    assert is_valid("123456") == 0

def test_haspoint():
    assert is_valid("PI3.14") == 0

def test_empty():
    assert is_valid("") == 0

def test_toolong():
    assert is_valid("50CS") == 0

def test_ok():
    assert is_valid("CS05") == 0

def test_nbbeforeend():
    assert is_valid("CS05CS") == 0

def test_nbbeforeend2():
    assert is_valid("05CSS") == 0
