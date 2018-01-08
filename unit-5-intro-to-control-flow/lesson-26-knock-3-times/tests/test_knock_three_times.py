def test_knock_three_times():
    with CaptureOutput() as output:
        knock_three_times()

    assert len(output) == 3
    assert output == [
        'Knock Knock',
        'Knock Knock',
        'Knock Knock'
    ]
