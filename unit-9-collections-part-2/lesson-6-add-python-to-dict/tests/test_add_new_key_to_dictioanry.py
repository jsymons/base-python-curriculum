def test_add_new_key_to_dictioanry():
    original = {
        "first_name": "jon",
        "last_name": "snow"
    }
    expected = {
        "first_name": "jon",
        "last_name": "snow",
        "fav_language": "python"
    }
    assert add_to_dictionary(original) == expected
