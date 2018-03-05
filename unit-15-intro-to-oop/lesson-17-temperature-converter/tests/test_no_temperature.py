import pytest

def test_no_temperature():
    with pytest.raises(NoTemperatureException):
        t = TempConverter()
