def test_list_of_duplicates():
    string = """Happy Python Programming Programming Programming Happy Me"""

    result = ["Happy", "Programming"]

    assert get_list_of_duplicates(count_words(string)) == result

