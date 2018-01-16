def test_count_occurrences_not_unique():
    assert count_occurrences(["a", "b", "c", "a", "a", "b"]) == {
        "a": 3,
        "b": 2,
        "c": 1
    }
