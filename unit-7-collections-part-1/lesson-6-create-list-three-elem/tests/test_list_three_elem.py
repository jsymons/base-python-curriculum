def test_list_three_elem():
    assert type(pizza_time) == list
    assert len(pizza_time) == 3
    assert pizza_time == [word1, word2, word3]
    assert type(word1) == str
    assert type(word2) == str
    assert type(word3) == str