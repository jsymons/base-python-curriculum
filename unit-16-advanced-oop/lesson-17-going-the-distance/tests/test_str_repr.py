def test_str_repr():
    d1 = Distance(4, "ft")
    d2 = Distance(1)

    list_of_distances =[d1, d2]

    assert str(d1) == "4ft"
    assert str(d2) == "1m"
    assert str(list_of_distances) == '[Distance: 4ft, Distance: 1m]'