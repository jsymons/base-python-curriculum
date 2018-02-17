box_5x8_expected = """
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
xxxxxxxx
""".lstrip()

def test_a_5x8_box():
    assert create_box(5, 8, 'x') == box_5x8_expected
