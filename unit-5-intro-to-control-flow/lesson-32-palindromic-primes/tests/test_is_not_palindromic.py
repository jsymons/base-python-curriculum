def test_is_not_palindromic():
    assert is_palindromic(123) is False
    assert is_palindromic(321) is False
    assert is_palindromic(28) is False
    assert is_palindromic(81239123) is False
