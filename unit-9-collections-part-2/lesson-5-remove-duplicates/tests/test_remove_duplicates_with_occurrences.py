def test_remove_duplicates_with_occurrences():
    assert remove_duplicates([1, 1, 1, 1, 1, 3, 4, 5, 5, 5]) == [1, 3, 4, 5]
