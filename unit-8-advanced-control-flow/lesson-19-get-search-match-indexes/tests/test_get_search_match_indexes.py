def test_get_search_match_indexes():
    assert get_search_match_indexes(["glasses", "suspicious", "pen", "suspicious"], "suspicious") == [1, 3]