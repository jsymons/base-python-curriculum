import pytest

def test_convert_invalid_units():
    c1 = Currency(1, 'USD')

    with pytest.raises(ValueError):
        c1.convert('NOT-FOUND')
