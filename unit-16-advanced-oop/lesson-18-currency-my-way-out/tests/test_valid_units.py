import pytest

def test_valid_units():
    # We can't create a Currency with a unit not present in the
    # USD_conversions dict
    with pytest.raises(ValueError):
        Currency(1, 'NOT-FOUND')
