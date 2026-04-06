import pytest
from seasons import validate_date

def test_validate_date_valid():
    assert validate_date("1999-01-01") == ("1999", "01", "01")
    assert validate_date("2024-12-31") == ("2024", "12", "31")

def test_validate_date_invalid_format():
    with pytest.raises(SystemExit):
        validate_date("January 1, 1999")

    with pytest.raises(SystemExit):
        validate_date("1999-1-1")

def test_validate_date_invalid_calendar():
    with pytest.raises(SystemExit):
        validate_date("2023-02-30")

    with pytest.raises(SystemExit):
        validate_date("2020-13-01")
