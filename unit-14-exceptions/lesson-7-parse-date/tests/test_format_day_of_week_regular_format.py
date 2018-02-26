def test_format_day_of_week_regular_format():
    assert parse_dates('Monday January 03, 2018') == datetime(2018, 1, 3)