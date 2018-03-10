def test_horse_str():
    talking_horse = Horse("Mr. Ed", "Saddlebred")
    sparkles = Horse("Charlie", "Unicorn")

    assert str(sparkles) == "Charlie the Unicorn"
    assert str(talking_horse) == "Mr. Ed the Saddlebred"