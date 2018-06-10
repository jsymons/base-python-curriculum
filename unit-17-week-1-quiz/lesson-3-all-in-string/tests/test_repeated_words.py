def test_repeated_words():
    a_string = "Python is good. Python is Wise. I like Python"
    assert all_in_string(a_string, 'Python', 'good', 'Ruby') == 2
