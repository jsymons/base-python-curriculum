def test_drive_not_electric():
    car1 = Car(electric=False)
    assert isinstance(car1, object) is True

    assert hasattr(car1, 'electric') is True

    assert car1.electric is False
    assert car1.drive() == 'VROOOOM'
