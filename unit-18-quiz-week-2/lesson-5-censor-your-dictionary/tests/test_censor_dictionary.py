def test_censor_dictionary():
    expressions = {
       "pumped": "I'm so darn excited!",
       "happy": "Yeehaw",
       "agreeable": "darn tootin!"
    }

    assert censor_dictionary(expressions, "darn") == {
        "happy": "Yeehaw"
    }
