def test_search_not_found():
    a_dict = {
        "a": "i",
        "b": "love",
        "c": "programming"
    }
    assert search_keys_for_value(a_dict, "howdy") == set()
