import pytest

def test_parse_number_invalid():
    with pytest.raises(ValueError):
        parse_number("invalid")