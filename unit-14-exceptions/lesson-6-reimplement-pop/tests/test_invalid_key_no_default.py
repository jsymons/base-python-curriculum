import pytest


test_dict = {
    "cat": "hat",
    "dog": "log",
    "elf": "shelf"
}


def test_invalid_key_no_default():
    with pytest.raises(KeyError):
        pop(test_dict, "horse")