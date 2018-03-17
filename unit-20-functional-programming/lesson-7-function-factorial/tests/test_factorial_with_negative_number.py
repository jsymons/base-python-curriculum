import pytest

def test_factorial_with_negative_number():
    """Should raise an exception"""
    with pytest.raises(ValueError):
        factorial(-1)
