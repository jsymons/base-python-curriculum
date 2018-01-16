def test_car1_attributes():
    assert isinstance(car1, Car) is True, 'car1 is not created'
    assert isinstance(car1, object) is True

    assert hasattr(car1, 'color') is True, "car1 doesn't have a color attribute"

    assert hasattr(car1, 'make') is True, "car1 doesn't have a make attribute"

    assert hasattr(car1, 'model') is True, "car1 doesn't have a model attribute"
