import pytest

def test_sum_with_no_elements_raises_error():
    with pytest.raises(AttributeError):
        sum_multiple()