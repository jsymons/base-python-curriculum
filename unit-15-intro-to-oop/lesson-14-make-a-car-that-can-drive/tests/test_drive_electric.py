def test_drive_electric():
    car2 = Car(electric=True)
    assert isinstance(car2, object) is True

    assert hasattr(car2, 'electric') is True

    assert car2.electric is True
    assert car2.drive() == 'WHIRRRRRRR'
