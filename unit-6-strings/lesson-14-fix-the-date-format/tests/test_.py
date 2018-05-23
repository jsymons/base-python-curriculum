def test_format():
    assert format_date(2018, 3, 20) == 'Today is 2018-3-20'
    assert format_date(2015, 1, 19) == 'Today is 2015-1-19'
