def test_overwrite_existing_key():
    assert add_to_dictionary({
        "fav_language": "elvish"
    }) == {
        "fav_language": "python"
    }
