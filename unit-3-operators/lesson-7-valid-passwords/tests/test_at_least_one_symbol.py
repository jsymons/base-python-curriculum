def test_at_least_one_symbol():
    assert at_least_one_symbol_pwd_1 is False
    assert at_least_one_symbol_pwd_2 is False
    assert at_least_one_symbol_pwd_3 is True
    assert at_least_one_symbol_pwd_4 is True
