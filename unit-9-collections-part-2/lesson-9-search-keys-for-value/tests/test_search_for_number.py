def test_search_for_number():
    a_dict = {
        "name": "billy",
        "age": 12,
        "fav_num": 12
    }
    assert search_keys_for_value(a_dict, 12) == {'fav_num', 'age'}
