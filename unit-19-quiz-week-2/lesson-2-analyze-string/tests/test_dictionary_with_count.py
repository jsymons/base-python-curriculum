def test_dictionary_with_count():
    string = """Happy Python Programming Programming Programming Happy Me"""

    assert count_words(string) == {"Me": 1, "Python": 1, "Programming": 3, "Happy": 2}