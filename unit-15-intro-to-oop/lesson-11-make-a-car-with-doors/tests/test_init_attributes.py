def test_init_attributes():
    car1 = Car(color='blue', number_of_doors=2)

    assert isinstance(car1, object) is True

    assert hasattr(car1, 'color') is True
    assert car1.color == 'blue'

    assert hasattr(car1, 'number_of_doors') is True
    assert car1.number_of_doors == 2
