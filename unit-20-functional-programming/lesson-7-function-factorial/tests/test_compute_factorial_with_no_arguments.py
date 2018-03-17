import pytest

def test_compute_factorial_with_no_arguments():
    """Should raise an exception"""
    with pytest.raises(ValueError):
        compute_factorial([])
