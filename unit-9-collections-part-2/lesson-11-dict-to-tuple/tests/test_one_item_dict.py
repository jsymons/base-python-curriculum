def test_one_item_dict():
    result = dict_to_tuple({'my_key': 20})
    expected = [('my_key', 20)]
    assert result == expected
