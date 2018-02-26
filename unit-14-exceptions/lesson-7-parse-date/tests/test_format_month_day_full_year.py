def test_format_month_day_full_year():
    assert parse_dates('January 03, 2018') == datetime(2018, 1, 3)