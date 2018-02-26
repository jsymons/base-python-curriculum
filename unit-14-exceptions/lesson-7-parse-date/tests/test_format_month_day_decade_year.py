def test_format_month_day_decade_year():
    assert parse_dates('January 03, 18') == datetime(2018, 1, 3)