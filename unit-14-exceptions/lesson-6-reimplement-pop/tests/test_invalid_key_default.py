test_dict = {
    "cat": "hat",
    "dog": "log",
    "elf": "shelf"
}


def test_invalid_key_default():
    assert pop(test_dict, "horse", "crickets") == "crickets"
    assert len(test_dict) == 3