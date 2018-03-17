import pytest

def test_factorial_terms_with_an_invalid_value():
    """Should raise an exception if an invalid number is provided"""
    with pytest.raises(ValueError):
        factorial_terms(-1)
