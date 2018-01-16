def test_car2_attributes():
    assert isinstance(car2, Car) is True, 'car2 is not created'
    assert isinstance(car2, object) is True

    assert hasattr(car2, 'color') is True, "car2 doesn't have a color attribute"

    assert hasattr(car2, 'make') is True, "car2 doesn't have a make attribute"

    assert hasattr(car2, 'model') is True, "car2 doesn't have a model attribute"
