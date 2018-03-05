def test_line():
    p1 = Point(0, 1)
    p2 = Point(1, 2)

    l = Line(p1, p2)

    assert l.slope() == 1
    assert l.y_intercept() == 1
    assert l.formula() == 'y = x + 1.0'