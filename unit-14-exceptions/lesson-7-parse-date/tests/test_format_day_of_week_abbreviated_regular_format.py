def test_format_day_of_week_abbreviated_regular_format():
    assert parse_dates('Mon January 03, 2018') == datetime(2018, 1, 3)