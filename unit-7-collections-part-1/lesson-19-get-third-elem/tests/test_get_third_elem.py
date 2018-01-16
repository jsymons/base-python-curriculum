def test_get_third_elem():
    assert get_third_elem(["not this one", "not this either", "this one!!!"]) == "this one!!!"