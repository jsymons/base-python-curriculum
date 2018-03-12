def test_one_occurrence_second_word():
    # Positions:
    #         0                         26      34
    phrase = "Python is good. Python is Wise. I like Python"
    assert positions(phrase, 'Javscript', 'like', 'Ruby') == "-,34,-"
