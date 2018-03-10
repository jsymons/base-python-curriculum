def test_calculate():
    obj1 = Loan(10)
    obj2 = Movie(5)
    obj3 = Milk(1)

    assert calculate(obj1, obj2) == 15
    assert calculate(obj1, obj3) == 11

    assert calculate(obj2, obj3) == 6

    assert calculate(obj3, obj3) == 2
