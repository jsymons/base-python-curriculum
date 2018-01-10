def test_default_num_doors():
    car2 = Car(color='green')
    assert isinstance(car2, object) is True

    assert hasattr(car2, 'color') is True
    assert car2.color == 'green'

    assert hasattr(car2, 'number_of_doors') is True
    assert car2.number_of_doors == 4
