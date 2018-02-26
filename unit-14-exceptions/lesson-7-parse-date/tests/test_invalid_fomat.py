import pytest


def test_invalid_fomat():
    with pytest.raises(ValueError):
        parse_dates('INVALID DATE')