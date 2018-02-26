def test_format_day_of_week_european_format():
    assert parse_dates('Monday 03 of January, 2018') == datetime(2018, 1, 3)