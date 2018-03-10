def test_horse_str():
    horse1 = Horse("Mr. Ed", "Saddlebred")
    horse2 = Horse("Charlie", "Unicorn")
    horse3 = Horse("Harry Trotter", "Clydesdale")

    horse_party = [horse1, horse2, horse3]

    assert str(horse_party) == '[Horse: Mr. Ed, Saddlebred, Horse: Charlie, Unicorn, Horse: Harry Trotter, Clydesdale]'