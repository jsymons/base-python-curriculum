import pytest

def test_area_invalid_unit():
    with pytest.raises(InvalidAreaUnitException):
        usa.area(unit='INVALID')
