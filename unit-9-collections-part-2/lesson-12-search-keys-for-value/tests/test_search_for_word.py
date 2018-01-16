def test_search_for_word():
    a_dict = {
        1: "hi",
        2: "there",
        3: "easter egg"
    }
    assert search_keys_for_value(a_dict, "easter egg") == {3}
