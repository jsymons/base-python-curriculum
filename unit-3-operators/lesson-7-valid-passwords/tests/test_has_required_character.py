def test_has_required_character():
    assert has_required_character_pwd_1 is False
    assert has_required_character_pwd_2 is True
    assert has_required_character_pwd_3 is True
    assert has_required_character_pwd_4 is True
