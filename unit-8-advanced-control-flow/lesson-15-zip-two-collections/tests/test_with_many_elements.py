def test_with_many_elements():
    result = rmotr_zip(['A', 'B', 'C'], [1, 2, 3])
    expected = [
      ('A', 1),
      ('B', 2),
      ('C', 3),
    ]

    assert result == expected
